a, b, c, d = map(int, input().split())
s = sorted([a, b, c])
print(max(0, d - abs(s[1] - s[0])) + max(0, d - abs(s[-1] - s[1])))
