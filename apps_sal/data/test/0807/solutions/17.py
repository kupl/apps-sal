n, c = list(map(int, input().split()))
v = list(map(int, input().split()))
ret = 0
for i in range(n - 1):
    ret = max(ret, v[i] - v[i + 1] - c)
print(ret)

