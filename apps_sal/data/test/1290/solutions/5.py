(n, m) = [int(i) for i in input().split()]
a = [0] * (n + 1)
b = [int(i) for i in input().split()]
for i in b:
    a[i] += 1
print(min(a[1:n + 1]))
