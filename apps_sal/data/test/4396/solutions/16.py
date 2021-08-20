N = int(input())
r = 380000
res = 0
for i in range(N):
    (x, u) = input().split()
    if u == 'JPY':
        res += int(x)
    else:
        res += float(x) * r
print(res)
