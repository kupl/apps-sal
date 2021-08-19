(n, k) = list(map(int, input().split()))
res = 1
while k & 1 == 0:
    k >>= 1
    res += 1
print(res)
