n, k = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
u = 100000000000000000000000000000000000000000000
m = 0
for i in range(k):
    if n % (s[i]) < u:
        u = n % (s[i])
        m = i
print(m + 1, n // (s[m]))
