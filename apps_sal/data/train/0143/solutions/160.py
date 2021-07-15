class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # length of the longest subarray containing at most 2 distinct elements
        if len(tree) == 0: return 0
        i, j, n_kind, res = 0, 0, 1, 1
        cnts = [0,] * len(tree)
        cnts[tree[0]] += 1
        while True:
            while n_kind <= 2:
                res = max(res, j-i+1)
                j += 1
                if j >= len(tree): 
                    return res  # ?
                if cnts[tree[j]] == 0:
                    n_kind += 1
                cnts[tree[j]] += 1
            while n_kind > 2:
                cnts[tree[i]] -= 1
                if cnts[tree[i]] == 0:
                    n_kind -= 1
                i += 1
        return res

