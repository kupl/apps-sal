from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        left_counts = {s[0]: 1}
        right_counts = Counter(s[1:])
        split_count = 0
        if len(list(left_counts.items())) == len(list(right_counts.items())):
            split_count += 1
        for i in range(1, len(s)):
            if s[i] in left_counts:
                left_counts[s[i]] += 1
            else:
                left_counts[s[i]] = 1
            if right_counts[s[i]] == 1:
                del right_counts[s[i]]
            else:
                right_counts[s[i]] -= 1
            if len(list(left_counts.items())) == len(list(right_counts.items())):
                split_count += 1
        return split_count
