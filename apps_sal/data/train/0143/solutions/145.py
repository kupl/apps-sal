class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res, start, distince_count, visited = 0, 0, 0, [0] * len(tree)
        for i, c in enumerate(tree):
            if visited[c] == 0:
                distince_count += 1
            visited[c] += 1

            while distince_count > 2:
                visited[tree[start]] -= 1
                if visited[tree[start]] == 0:
                    distince_count -= 1

                start += 1

            res = max(res, i - start + 1)

        return res
