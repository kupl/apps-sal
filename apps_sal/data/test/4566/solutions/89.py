N, M = list(map(int, input().split()))
ans = [0 for i in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    ans[a - 1] += 1
    ans[b - 1] += 1

for x in ans:
    print(x)
