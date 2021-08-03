g, a = [int(x) for x in input().split()]
b = c = a
s = 0
while min(min(a, b), c) < g:
    s += 1
    l = [a, b, c]
    l.sort()
    a, b, c = l
    a = min(g, c + b - 1)
print(s)
