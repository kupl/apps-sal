class Solution:
    def numSplits(self, s: str) -> int:
        le_set, ri_set = [s[0]], [s[-1]]
        le_arr, ri_arr = [1] * len(s), [1] * len(s)
        # print(le_arr[0])
        # print(ri_arr)
        for i in range(1, len(s)):
            le_arr[i] = le_arr[i - 1]
            if s[i] not in le_set:
                le_set.append(s[i])
                le_arr[i] += 1

        for i in range(len(s) - 2, -1, -1):
            ri_arr[i] = ri_arr[i + 1]
            if s[i] not in ri_set:
                ri_set.append(s[i])
                ri_arr[i] += 1

        # print(le_arr)
        # print(ri_arr)
        cnt = 0
        for i in range(0, len(s) - 1):
            if le_arr[i] == ri_arr[i + 1]:
                cnt += 1
        return cnt
