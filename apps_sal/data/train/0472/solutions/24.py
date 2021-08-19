class Solution:

    def canReach(self, jumps: List[int], start: int) -> bool:
        size = len(jumps)
        reach = [[] for i in range(size)]
        for (pos, jump) in enumerate(jumps):
            (l, r) = (pos - jump, pos + jump)
            if l >= 0 and pos not in reach[l]:
                reach[l].append(pos)
            if r < size and pos not in reach[r]:
                reach[r].append(pos)

        def do(idx, path=set()):
            if idx == start:
                return True
            for prev in reach[idx]:
                if prev not in path and do(prev, path | {prev}):
                    return True
            return False
        for (p, n) in enumerate(jumps):
            if n == 0 and do(p):
                return True
        return False
