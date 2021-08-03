from collections import Counter
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 7)


class HeapSet:
    def __init__(self):
        self.minQue = []
        self.maxQue = []
        self.counter = Counter()

    def insert(self, x):
        heappush(self.minQue, x)
        #heappush(self.maxQue, -x)
        self.counter[x] += 1

    def erase(self, x):
        self.counter[x] -= 1

    def max(self):
        while self.maxQue and self.counter[-self.maxQue[0]] == 0:
            heappop(self.maxQue)
        return -self.maxQue[0] if self.maxQue else None

    def min(self):
        while self.minQue and self.counter[self.minQue[0]] == 0:
            heappop(self.minQue)
        return self.minQue[0] if self.minQue else None


MOD = 998244353


def resolve():
    def dfs(v):
        res = 1
        for to in to_edge[v]:
            res *= dfs(to)
            res %= MOD
        return res + 1

    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort()
    st = HeapSet()
    to_edge = [[] for _ in range(N)]
    # treeを作成
    for i in range(N - 1, -1, -1):
        x = AB[i][0]  # 初期位置
        d = AB[i][1]  # 移動距離

        while st.min() and st.min()[0] < x + d:
            to_edge[i].append(st.min()[1])
            st.erase(st.min())
        st.insert((x, i))  # 初期位置、頂点番号

    ans = 1
    for (x, v) in st.minQue:
        ans *= dfs(v)
        ans %= MOD
    print(ans)


def __starting_point():
    resolve()


__starting_point()
