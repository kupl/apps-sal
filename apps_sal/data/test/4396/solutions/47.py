n = int(input())
ans = 0
for _ in range(n):
    (x, u) = input().split()
    if u == 'JPY':
        x = int(x)
        ans += x
    else:
        x = float(x)
        tmp = x * 380000
        ans += tmp
print(ans)
