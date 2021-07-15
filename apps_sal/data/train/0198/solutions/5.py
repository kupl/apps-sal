class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        prefix = [0] # prefix[i] gives us cost[0] + ... + cost[i-1]
        for i in range(len(cost)):
            prefix.append(prefix[-1]+cost[i])
        maxLen = 0
        i,j = 0,0
        # print(prefix)
        while j < len(cost):
            while j < len(cost) and prefix[j+1]-prefix[i] <= maxCost:
                j += 1
            maxLen = max(maxLen,j-i)
            i += 1
            # j = i
            if i > j:
                j = i
        return maxLen
