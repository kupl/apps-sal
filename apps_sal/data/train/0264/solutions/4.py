class Solution:
    def get_max_length(self, sets, idx, cur_set):
        if idx == len(sets): return len(cur_set)
        m = 0
        for i in range(idx, len(sets)):
            if not cur_set & sets[i]:
                res = self.get_max_length(sets, i + 1, cur_set.union(sets[i]))
            else:
                res = self.get_max_length(sets, i + 1, cur_set)
            m = max(m, res)
        return m
        
    
    def maxLength(self, arr: List[str]) -> int:
        sets = []
        for i, s in enumerate(arr):
            t = set()
            for ch in s:
                if ch in t:
                    break
                else:
                    t.add(ch)
            else:
                sets.append(t)
        print(sets)
        return self.get_max_length(sets, 0, set())

