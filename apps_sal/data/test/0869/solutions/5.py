(a, b) = map(int, input().split())
a1 = min(a, b)
c = max(a, b)
c -= a1
a2 = c // 2
print(a1, a2)
