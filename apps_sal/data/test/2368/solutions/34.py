import sys
readline = sys.stdin.readline

N, M = list(map(int, readline().split()))
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

G = [[] for i in range(N)]
for i in range(M):
    c, d = list(map(int, readline().split()))
    G[c - 1].append(d - 1)
    G[d - 1].append(c - 1)

seen = set()
for i in range(N):
    if i in seen:
        continue
    stack = [i]
    a_sum = 0
    b_sum = 0
    while stack:
        v = stack.pop()
        if v in seen:
            continue
        seen.add(v)
        a_sum += A[v]
        b_sum += B[v]
        for child in G[v]:
            stack.append(child)
    if a_sum != b_sum:
        print("No")
        break
else:
    print("Yes")
