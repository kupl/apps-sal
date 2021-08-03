n = int(input())
res = 0.0
for _ in range(n):
    x, u = input().split()
    x = float(x)
    res += x if u == 'JPY' else x * 380000.0
print(res)
