bit = 380000.0
n = int(input())
ans = 0
for i in range(n):
    (x, u) = input().split()
    x = float(x)
    if u == 'JPY':
        ans += x
    else:
        ans += x * bit
print(ans)
