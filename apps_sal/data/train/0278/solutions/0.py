class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        counts = Counter(digits)
        m = sum(digits) % 3
        if m:
            if counts[m] + counts[m + 3] + counts[m + 6]:
                counts[min([m + i for i in [0, 3, 6] if counts[m + i]])] -= 1
            else:
                counts[min([i - m for i in [3, 6, 9] if counts[i - m]])] -= 1
                counts[min([i - m for i in [3, 6, 9] if counts[i - m]])] -= 1

        ans = ''
        for i in range(9, -1, -1):
            if not ans and not counts[i]:
                continue
            ans += str(i) * counts[i]
        if ans:
            return ans.lstrip('0') or '0'
        return ''
