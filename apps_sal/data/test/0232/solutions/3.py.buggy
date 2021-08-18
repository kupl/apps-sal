n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
k = [int(i) for i in input().split()]
for i in range(n):
    for j in range(i + 1, n + 1):
        cur = a[i:j]
        c = [0] * m
        for l in cur:
            c[l - 1] += 1
        if c == k:
            print("YES")
            return
print("NO")
