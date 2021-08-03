class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        left = len(s) * [0]
        right = len(s) * [0]
        seen = set(s[0])
        # right[-1] = 1
        left[0] = 1
        for i in range(1, len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                left[i] = left[i - 1] + 1
            else:
                left[i] = left[i - 1]
        seen = set()
        rtotal = 0
        count = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] not in seen:
                seen.add(s[i])
                rtotal += 1
            if rtotal == left[i - 1]:
                count += 1
            elif rtotal > left[i - 1]:
                break

        # count = 0
        # # print(left)
        # # print(right)
        # for i in range(0, len(s)-1):
        #     if left[i]== right[i+1]:
        #         count +=1
        #     elif right[i+1] < left[i]:
        #         break

        return count
