class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i = 0
        next_start_pos = None
        max_len = 0
        s = set()
        res = []
        while i < len(tree):
            if tree[i] in s:
                max_len += 1
                i += 1
            else:
                if len(s) == 0:
                    s.add(tree[i])
                    max_len += 1
                    i += 1
                elif len(s) == 1:
                    s.add(tree[i])
                    max_len += 1
                    next_start_pos = i
                    i += 1
                elif len(s) == 2:
                    res.append(max_len)
                    max_len = 0
                    s = set()
                    i = next_start_pos
                    
        res.append(max_len)
        return max(res)
