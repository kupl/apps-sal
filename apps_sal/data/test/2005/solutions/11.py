n, n1, n2 = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)

n1, n2 = min(n1, n2), max(n1, n2)

a1 = sum(a[0:n1]) / n1
a2 = sum(a[n1:n1 + n2]) / n2
print(a1 + a2)
