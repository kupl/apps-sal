import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
ans = [0] * N

for i in range(M):
    ab = list(map(int, readline().split()))
    for a in ab:
        ans[a - 1] += 1

for a in ans:
    print(a)
