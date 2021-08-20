class Solution:

    def totalFruit(self, s: List[int]) -> int:
        m = 0
        arr = {}
        i = 0
        k = 2
        for j in range(len(s)):
            if s[j] not in arr:
                arr[s[j]] = 0
            arr[s[j]] += 1
            while len(arr) > k:
                x = s[i]
                arr[x] -= 1
                if arr[x] == 0:
                    arr.pop(x)
                i += 1
            m = max(m, j - i + 1)
        return m
