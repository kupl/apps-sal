a, b, c, d = list(map(int, input().split()))
s = [a, b, c]
s.sort()
a, b, c = s
print(max(0, a - b + d) + max(0, b - c + d))
