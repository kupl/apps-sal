N = int(input())
P = list(map(int, input().split()))

cnt = 0

for p in P:
    cnt += p <= N
    N = min(N, p)

print(cnt)
