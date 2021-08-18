N = int(input())
A = list(map(int, input().split()))
ans = [0 for _ in range(N)]
for i in reversed(range(N - 1)):
    boss = A[i] - 1
    ans[boss] += 1
for x in ans:
    print(x)
