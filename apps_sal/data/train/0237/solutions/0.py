class Solution:
    def numSubarraysWithSum(self, pl, S):
        ans = 0

        if(S == 0):
            c = 0
            for i in range(len(pl)):
                if(pl[i] == 0):
                    c += 1
                else:
                    c = 0
                ans += c
            return ans

        l = [-1]

        for i in range(len(pl)):
            if(pl[i] == 1):
                l.append(i)

        l.append(len(pl))

        ans = 0

        for i in range(1, len(l) - S):

            ans += (l[i] - l[i - 1]) * (l[i + S] - l[i + S - 1])

        return ans
