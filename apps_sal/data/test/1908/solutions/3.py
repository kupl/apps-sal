from collections import deque
import sys


def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]


def main():
    n, m = MI()
    ww = LI()
    xy = LLI1(m)
    fav_mem = [[] for _ in range(n)]
    fav_cnt = [0] * n
    for j, (x, y) in enumerate(xy):
        fav_mem[x].append(j)
        fav_mem[y].append(j)
        fav_cnt[x] += 1
        fav_cnt[y] += 1

    q = deque()
    for i in range(n):
        if ww[i] - fav_cnt[i] >= 0:
            q.append(i)

    ans = []
    fini = [False] * n
    finj = [False] * m
    while q:
        i = q.popleft()
        for j in fav_mem[i]:
            if finj[j]:
                continue
            ans.append(j + 1)
            finj[j] = True
            for i0 in xy[j]:
                if fini[i0]:
                    continue
                fav_cnt[i0] -= 1
                if ww[i0] - fav_cnt[i0] >= 0:
                    q.append(i0)
                    fini[i0] = True
    if len(ans) == m:
        print("ALIVE")
        print(*ans[::-1])
    else:
        print("DEAD")


main()
