n = int(input())
a = list(map(int, input().split(' ')))
s = 0
for i in range(0, n):
    for j in range(i, n):
        t = 0
        for k in range(0, n):
            t += a[k] ^ (k >= i and k <= j)
        s = max(s, t)
print(s)
