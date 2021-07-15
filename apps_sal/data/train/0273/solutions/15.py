class Solution:
    def racecar(self, target: int) -> int:
        layer = collections.deque([(0,1)])
        visited = set()
        ans = 0
        while len(layer) > 0:
            nxt_layer = collections.deque()
            while len(layer) > 0:
                p, s = layer.popleft()
                if p > target*2 and s > target*2:
                    continue
                if p == target:
                    return ans
                nxt_a = (p+s, 2*s)
                if nxt_a not in visited:
                    nxt_layer.append(nxt_a)
                    visited.add(nxt_a)
                nxt_r = (p, -1 if s > 0 else 1)
                if nxt_r not in visited:
                    nxt_layer.append(nxt_r)
                    visited.add(nxt_r)
            layer= nxt_layer
            ans+=1
