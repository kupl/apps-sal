a, b, c = map(int, input().split())
m = max(a, b, c)
s = (m - a) + (m - b) + (m - c)
if s % 2 == 0:
    print(s // 2)
else:
    print(1 + (s + 1) // 2)
