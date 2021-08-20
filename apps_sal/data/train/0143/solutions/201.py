class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        N = len(tree)
        cache = Counter()
        left = right = 0
        maxx = 0
        while left < N and right < N:
            curr = tree[right]
            cache[curr] += 1
            while len(cache) > 2 and left < N:
                curr = tree[left]
                cache[curr] -= 1
                if cache[curr] <= 0:
                    del cache[curr]
                left += 1
            maxx = max(maxx, right - left + 1)
            right += 1
        return maxx
