(n, m) = map(int, input().split())
a = [int(e) % 2 for e in input().split()]
b = [int(e) % 2 for e in input().split()]
a1 = sum(a)
a0 = n - a1
b1 = sum(b)
b0 = m - b1
print(min(a1, b0) + min(a0, b1))
