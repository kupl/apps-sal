n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for l, r in A:
    ans += r - l + 1
print(ans)
