class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        max_len = 0
        start = end = 0
        N = len(tree)
        count = 0
        uniq = {}

        while end < N:
            cur = tree[end]
            if cur not in uniq:
                uniq[cur] = 0

            uniq[cur] += 1
            if uniq[cur] == 1:
                count += 1

            while count > 2:
                rem = tree[start]
                uniq[rem] -= 1
                if uniq[rem] == 0:
                    count -= 1
                start += 1

            max_len = max(max_len, end - start + 1)
            end += 1

        return max_len
