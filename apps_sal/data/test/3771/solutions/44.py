# 最大流
# https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
from collections import deque
import sys
sys.setrecursionlimit(10**7)


class MaxFlow:
    # n:頂点数
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in range(n)]

    # 辺を追加する
    # fr:辺の始点
    # to:辺の終点
    # cap:辺のキャパシティ
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        # forward[2]=backward,backward[2]=forwardとなるように再帰的にforwardとbackwardを定義
        self.g[fr].append(forward)
        self.g[to].append(backward)
        # print('add_edge',fr,to)

    # sから各頂点への距離を返す。フローを流すごとにcapが減り、最終的に通れる辺が減り、tまで辿り着けなくなる。それまでフローを流す
    def bfs(self, s, t):
        self.level = level = [None] * self.n
        deq = deque([s])
        level[s] = 0
        g = self.g
        while deq:
            v = deq.popleft()
            nlv = level[v] + 1
            for nv, cap, _ in g[v]:
                if cap and level[nv] is None:
                    level[nv] = nlv
                    deq.append(nv)
        return level[t] is not None
    # v->tにfを流す。再帰的に呼び出す。v=tとなるまで続ける。
    # sから遠ざかるようなパスを見つけ、フローを流す

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        # self.it[v]:頂点vから伸びる辺。一本の辺について着目するとfordwardとbackwardが交互に呼び出される。
        for e in self.it[v]:
            nv, cap, rev = e
            if cap and level[v] < level[nv]:
                d = self.dfs(nv, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    # sからtへの最大フローを返す。
    # 以下の処理をフローを流しきるまで繰り返す。
    # BFSでsourceから各頂点までの距離(level)を計算
    # DFSでsourceからの距離が遠くなるようなパスを見つけ、フローを流す
    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        g = self.g
        # sから各頂点への距離を計算。sからtへ辿り着けない場合、終了。距離はself.levelに保存される。
        while self.bfs(s, t):
            # グラフの各要素をイテレータに変換ものをself.itに入れる。????
            *self.it, = list(map(iter, self.g))
            f = INF
            while f:
                # s->tにフローを流す。流せた量をflowに加算。流せる量があるまで続ける。
                f = self.dfs(s, t, INF)
                flow += f
        return flow


def main2(h, w, mat):
    ss = -1, -1
    tt = -1, -1
    n = h + w + 2
    g = [[] for _ in range(n)]
    ary = []
    inf = 10**18
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 'o':
                ary.append([i, h + j, 1])
                ary.append([h + j, i, 1])
            elif mat[i][j] == 'S':
                ary.append([h + w, i, inf])
                ary.append([i, h + w, inf])
                ary.append([h + w, h + j, inf])
                ary.append([h + j, h + w, inf])
                ss = i, j
            elif mat[i][j] == 'T':
                ary.append([h + w + 1, i, inf])
                ary.append([i, h + w + 1, inf])
                ary.append([h + w + 1, h + j, inf])
                ary.append([h + j, h + w + 1, inf])
                tt = i, j
    if ss[0] == tt[0] or ss[1] == tt[1]: return -1
    mf = MaxFlow(n)
    for i, j, c in ary:
        mf.add_edge(i, j, c)
    ret = mf.flow(h + w, h + w + 1)
    return ret


def __starting_point():
    h, w = list(map(int, input().split()))
    mat = [list(input()) for _ in range(h)]
    ret2 = main2(h, w, [x.copy() for x in mat])
    print(ret2)


__starting_point()
