s = input()
n = len(s)
(x, a, b) = (0, 0, 0)
for i in range(n):
    if s[i] == '-':
        x -= 1
    else:
        x += 1
    a = min(a, x)
    b = max(b, x)
print(b - a)
