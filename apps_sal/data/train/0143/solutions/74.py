class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        n = len(tree)
        res = 1
        last_occur = {tree[0]: 0}
        (i, j) = (0, 1)
        while j < n:
            new_type = tree[j]
            if new_type in last_occur or len(last_occur.keys()) < 2:
                last_occur[new_type] = j
                res = max(res, j - i + 1)
            else:
                count = j - i
                res = max(res, count)
                keys = list(last_occur.keys())
                t = keys[0] if last_occur[keys[0]] < last_occur[keys[1]] else keys[1]
                i = last_occur[t] + 1
                del last_occur[t]
                last_occur[new_type] = j
            j += 1
        return res
