n, l = list(map(int, input().split()))
s = [i + l - 1 for i in range(1, n + 1)]
x = sum(s)
s.sort(key=lambda y: abs(y))
print((x - s[0]))
