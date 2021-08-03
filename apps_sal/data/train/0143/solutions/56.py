class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, r, ans = 0, 0, 0
        counter = Counter()
        length = 0
        while r < len(tree):
            counter[tree[r]] += 1
            length = len(counter)
            r += 1

            while length > 2:
                counter[tree[l]] -= 1
                if counter[tree[l]] == 0:
                    del counter[tree[l]]
                    length -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
