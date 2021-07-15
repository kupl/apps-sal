n = int(input())
c = list(map(int, input().split()))
ans = 0
osn = 0
for i in range(n):
    if c[i] <= osn * 2:
        ans += c[i] // 2
        osn += c[i] % 2 - c[i] // 2
    else:
        osn += c[i]
        ans += osn // 3
        osn %= 3
print(ans)
