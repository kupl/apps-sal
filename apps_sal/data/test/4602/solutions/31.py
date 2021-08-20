N = int(input())
K = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(N):
    a = abs(x[i]) * 2
    b = abs(K - x[i]) * 2
    ans += min(a, b)
print(ans)
