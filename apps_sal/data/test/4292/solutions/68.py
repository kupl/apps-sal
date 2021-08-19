(n, k) = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
d = 0
for a in range(k):
    d = d + b[a]
print(d)
