class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        for answer in range(len(s), 0, -1):
            num_splits = answer - 1
            for split_points in combinations(range(1, len(s)), num_splits):
                current = 0
                words = set()
                for split_point in split_points:
                    words.add(s[current:split_point])
                    current = split_point
                words.add(s[current:])
                if len(words) == answer:
                    return answer
