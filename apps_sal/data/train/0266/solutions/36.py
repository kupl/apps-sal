class Solution:
    def numSplits(self, s: str) -> int:
        count = 0
        left, right = defaultdict(int), Counter(s)
        count = 0
        for letter in s:
            left[letter] += 1
            right[letter] -= 1
            if right[letter] == 0:
                del right[letter]
            count += (len(left) == len(right))
        return count
