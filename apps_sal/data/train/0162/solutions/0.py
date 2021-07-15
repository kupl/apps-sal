class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        last, current = [0] * (len(b) + 1), [0] * (len(b) + 1)
        
        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                if a[i] == b[j]:
                    current[j] = 1 + last[j + 1]
                else:
                    current[j] = max(last[j], current[j + 1])
            last = current
            current = [0] * (len(b) + 1)
        return last[0]
