(k, n, w) = list(map(int, input().split()))
res = 0
for i in range(1, w + 1):
    res += i * k
if n < res:
    print(res - n)
else:
    print(0)
