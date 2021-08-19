n = int(input())
m = int(input()[::-1], 2)
l = m + 1 & (1 << n) - 1
res = 0
for i in range(n):
    if m & 1 != l & 1:
        res += 1
    l >>= 1
    m >>= 1
print(res)
