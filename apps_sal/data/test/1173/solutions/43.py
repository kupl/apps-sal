import itertools
N = int(input())
A = [[int(_) - 1 for _ in input().split()][::-1] for _ in range(N)]
ans = 0
cand = list(range(N))
left = 1
while True:
    cand_ = set()
    for i in cand:
        v = A[i]
        if not len(v):
            continue
        if A[v[-1]][-1] == i:
            f = 0
            cand_.add(i)
            cand_.add(v[-1])
    if not cand_:
        break
    cand = cand_
    left = 0
    for i in cand:
        A[i].pop()
        left |= len(A[i]) > 0
    ans += 1
if left:
    print((-1))
else:
    print(ans)
