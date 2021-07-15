n = int(input())
a = 0
for _ in range(n):
    x, u = map(str, input().split())
    if u == 'JPY':
        a += int(x)
    else:
        a += float(x) * 380000
print(a)
