from collections import deque
N = int(input())


def proc(x):
    return int(x) - 1


A = [deque(list(map(proc, input().split())) + [-1]) for i in range(N)]

ans = 0
rest = N * (N - 1)
cand = set(range(N))
while rest > 0:
    cand_next = set()
    for n in cand:
        if A[A[n][0]][0] == n:
            cand_next.add(n)
    if len(cand_next) == 0:
        ans = -1
        break
    rest -= len(cand_next)
    cand = set()
    for n in cand_next:
        A[n].popleft()
        cand.add(n)
        if A[n][0] != -1:
            cand.add(A[n][0])
    ans += 1


print(ans)
