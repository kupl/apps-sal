from collections import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))

class Dinic():
    def __init__(self, n, s, t):
        self.n, self.s, self.t = n, s, t
        self.to = defaultdict(list)
        self.level = [-1]
        self.max_flow = -1

    def add_edge(self, u, v, cap):
        u_index_in_to_v = len(self.to[v])
        v_index_in_to_u = len(self.to[u])
        self.to[u].append([v, cap, u_index_in_to_v])
        self.to[v].append([u, 0, v_index_in_to_u])

    def set_level(self):
        s = self.s
        level = [-1] * self.n
        level[s] = 0
        q = deque()
        q.append([s, 0])
        while q:
            u, u_level = q.popleft()
            for v, cap, _ in self.to[u]:
                if cap == 0: continue
                if level[v] != -1: continue
                level[v] = u_level + 1
                if v == self.t:
                    self.level=level
                    return True
                q.append([v, u_level + 1])
        return False

    def dfs(self, u=-1, flow_to_me=10 ** 16):
        if u == -1: u = self.s
        if u == self.t: return flow_to_me
        flow_from_me = 0
        u_level = self.level[u]
        for utov_i, (v, cap, vtou_i) in enumerate(self.to[u]):
            if self.level[v] != u_level + 1: continue
            if cap == 0: continue
            flow_to_v = self.dfs(v, min(cap, flow_to_me - flow_from_me))
            if not flow_to_v: continue
            flow_from_me += flow_to_v
            self.to[u][utov_i][1] -= flow_to_v
            self.to[v][vtou_i][1] += flow_to_v
        return flow_from_me

    def calculation(self):
        res = 0
        while self.set_level():
            res += self.dfs()
        return res

    # これが出力用
    def get_max_flow(self):
        if self.max_flow == -1:
            self.max_flow = self.calculation()
        return self.max_flow

def main():
    n = int(input())
    aa = LI()
    mf = Dinic(n + 2, 0, n + 1)
    max_sum = 0
    for i, a in enumerate(aa, 1):
        if a > 0:
            mf.add_edge(i, n + 1, a)
            max_sum += a
        else:
            mf.add_edge(0, i, -a)
    for i in range(1, n // 2 + 1):
        for j in range(i * 2, n + 1, i):
            mf.add_edge(i, j, 10 ** 12)
    print(max(0, max_sum - mf.get_max_flow()))

main()

