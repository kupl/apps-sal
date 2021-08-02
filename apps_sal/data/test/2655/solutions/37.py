n = int(input())
a = [int(i) for i in input().split()]
a.sort()

ans = 0
for i in range(1, n):
    if i == 1:
        ans += a[-i]
    else:
        ans += a[-((i - 2) // 2 + 2)]
print(ans)
