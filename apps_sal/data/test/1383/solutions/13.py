n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for j in range(n):
    c = b[j:] + b[:j]
    diff = []
    for i in range(n):
        diff.append((c[i] - a[i]) % m)
    if diff.count(diff[0]) == n:
        print(diff[0] % m)
        break
