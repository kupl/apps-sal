class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def helper(start):
            nonlocal seen, s
            length = len(s)
            if start == length:
                return 0

            max_split, cur_split = 0, 0
            for split in range(start + 1, length):
                left, right = s[start:split], s[split:length]
                if left in seen or right in seen or left == right:
                    continue
                seen.add(left)
                cur_split = 1 + helper(split)
                seen.remove(left)
                max_split = max(max_split, cur_split)

            return max_split

        return 1 + helper(0)
