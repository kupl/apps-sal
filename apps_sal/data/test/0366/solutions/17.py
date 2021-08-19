(n, s) = map(int, input().split())
res = 0
for i in range(n, 0, -1):
    res += s // i
    s = s % i
print(res)
