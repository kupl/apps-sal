n = int(input())
c = list(map(int, input().split()))
c = [0] + c + [0]
ans = 0
for i in range(n + 1):
    ans += abs(c[i + 1] - c[i])
for i in range(n):
    d = abs(c[i + 1] - c[i]) + abs(c[i + 2] - c[i + 1])
    e = abs(c[i + 2] - c[i])
    print(ans - d + e)
