N = int(input())
p = [int(input()) for i in range(N)]

ans = 0
for i in range(N):
    ans += p[i]

ans -= max(p) // 2

print(ans)
