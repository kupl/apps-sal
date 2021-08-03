n, n1, n2 = [int(item) for item in input().split()]

a = [int(item) for item in input().split()]

a = sorted(a)
n1, n2 = min(n1, n2), max(n1, n2)
s1 = sum(a[n - n1:]) / n1
s2 = sum(a[n - n1 - n2:n - n1]) / n2

print(s1 + s2)
