class Solution:
    # Use an index to store where
    #       score - 1            score
    # |-----------|----------------|
    #             |--------1-------|
    def longestWPI(self, hours: List[int]) -> int:
        score, longest = 0, 0
        index = {}
        for i, n in enumerate(hours):
            score += 1 if n > 8 else -1
            if score > 0:  # more tiring days so far
                longest = max(longest, i + 1)
            index.setdefault(score, i)  # record the earliest presum with score
            if score - 1 in index:
                longest = max(longest, i - index[score - 1])
        return longest
