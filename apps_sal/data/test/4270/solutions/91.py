n = int(input())
v = sorted(list(map(int, input().split())))
res = v[0]
for i in range(n - 1):
    res = (res + v[i + 1]) / 2
print(res)
