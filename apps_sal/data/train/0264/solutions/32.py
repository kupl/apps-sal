class Solution:

    def maxLength(self, arr: List[str]) -> int:

        def maxLength(i, string):
            nonlocal ans
            if i == len(arr):
                (s, invalid) = (set(), False)
                for ch in string:
                    if ch in s:
                        invalid = True
                        break
                    s.add(ch)
                if not invalid:
                    ans = max(ans, len(string))
                return
            maxLength(i + 1, string)
            maxLength(i + 1, string + arr[i])
        ans = 0
        maxLength(0, '')
        return ans
