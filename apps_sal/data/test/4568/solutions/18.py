n = int(input())
s = input()
c = 0
for i in range(1, n - 1):
    x = set(s[:i])
    y = set(s[i:])
    cap = x & y
    c = max(c, len(cap))
print(c)
