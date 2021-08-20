a = [int(x) for x in input().split()]
(n, k) = (a[0], a[1])
a = [int(x) for x in input().split()]
n = 5 - k
ch = 0
for i in a:
    if i <= n:
        ch += 1
print((ch - ch % 3) // 3)
