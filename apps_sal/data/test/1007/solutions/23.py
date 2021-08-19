(k, p) = list(map(int, input().strip().split()))
res = 0
for i in range(1, k + 1):
    x = str(i)
    x = x + x[::-1]
    res = (res + int(x)) % p
print(res)
