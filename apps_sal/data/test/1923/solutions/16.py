N = int(input())
L = sorted(map(int, input().split()))

ans = 0
for i in range(N):
    ans += L[i * 2]

print(ans)

