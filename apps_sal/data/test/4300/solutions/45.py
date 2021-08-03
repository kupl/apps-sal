n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(len(d) - 1):
    for k in range(i + 1, len(d)):
        ans += d[i] * d[k]

print(ans)
