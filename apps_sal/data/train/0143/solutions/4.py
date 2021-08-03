class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        window = collections.Counter()
        ans = 0

        left = 0
        for right in range(len(tree)):
            window[tree[right]] += 1
            while len(window) > 2:
                window[tree[left]] -= 1
                if window[tree[left]] == 0:
                    del window[tree[left]]
                left += 1

            ans = max(ans, sum(window.values()))

        return ans
