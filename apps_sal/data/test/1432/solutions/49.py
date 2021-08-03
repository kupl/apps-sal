n = int(input())
aa = list(map(int, input().split()))

x = 0
for i in range(n):
    if i % 2 == 0:
        x += aa[i]
    else:
        x -= aa[i]

ans = [x]
for i in range(n - 1):
    x = 2 * (aa[i] - x // 2)
    ans.append(x)
print(*ans)
