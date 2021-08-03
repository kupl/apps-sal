n, k = map(int, input().split())

r = n // k
res = r ** 3
if k % 2 == 0:
    s = r
    if n % k >= k // 2:
        s += 1
    res += s ** 3
print(res)
