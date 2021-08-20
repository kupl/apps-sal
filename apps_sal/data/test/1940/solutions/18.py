(n, k) = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]
w.sort()
m = 0
for i in w:
    m += (i + k - 1) // k
print((m + 1) // 2)
