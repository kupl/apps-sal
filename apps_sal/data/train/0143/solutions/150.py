class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        letter_count = collections.defaultdict(int)
        (left, right) = (0, 0)
        while right < len(tree):
            letter_count[tree[right]] += 1
            right += 1
            if len(letter_count) > 2:
                letter_count[tree[left]] -= 1
                if letter_count[tree[left]] == 0:
                    del letter_count[tree[left]]
                left += 1
        return right - left
