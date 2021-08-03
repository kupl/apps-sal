s, c = map(int, input().split())
p = s * 2
if p <= c:
    print(s + (c - p) // 4)
else:
    print(c // 2)
