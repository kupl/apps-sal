class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos = sorted(pos)
        
        def test(gap, pos = pos, m = m):
            cur = pos[0]
            i = 1
            m -= 1
            while i < len(pos):
                if pos[i] - cur >= gap:
                    cur = pos[i]
                    m -= 1
                    if m == 0: return True
                i += 1
            return False
        
        lower, upper = 1, pos[-1]-pos[0]
        if test(upper): return upper
        while True:
            gap = (lower + upper) // 2
            if test(gap): lower = gap
            else: upper = gap
            if upper - lower == 1: return lower
