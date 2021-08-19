(n, k) = map(int, input().split())
res = 0
while k % 2 == 0:
    k /= 2
    res += 1
print(res + 1)
