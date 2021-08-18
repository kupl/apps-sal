from sys import stdin

n, n1, n2 = list(map(int, stdin.readline().split()))

a = sorted(map(int, stdin.readline().split()), key=lambda x: -x)

mn = min(n1, n2)
mx = max(n1, n2)

print((sum(a[:mn]) / mn) + (sum(a[mn:mn + mx]) / mx))
