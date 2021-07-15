import sys
N, M, Q = map(int, input().split())
abcd = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]
ans = 0
done = set()
todo = [(i,) for i in range(1, M + 1)]
while todo:
    A = todo.pop()
    done.add(A)
    if len(A) == N:
        total = 0
        for a, b, c, d in abcd:
            if A[b-1] - A[a-1] == c:
                total += d
        ans = max(ans, total)
        continue
    for i in range(A[-1], M + 1):
        nA = A + (i,)
        if not nA in done:
            todo.append(nA)
print(ans)
