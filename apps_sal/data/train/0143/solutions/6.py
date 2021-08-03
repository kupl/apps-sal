class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = 0
        max_elem_count = 0
        window = {}
        start = 0

        l = len(tree)
        for end in range(l):
            if tree[end] in window:
                window[tree[end]] += 1
            else:
                window[tree[end]] = 1
            max_elem_count = max(max_elem_count, window[tree[end]])

            while len(window) > 2:
                window[tree[start]] -= 1
                if window[tree[start]] == 0:
                    window.pop(tree[start])
                start += 1

            res = max(res, end - start + 1)

        return res
