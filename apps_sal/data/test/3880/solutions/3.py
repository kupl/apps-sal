(n, t) = (int(input()), list(map(int, input().split())))
p = list(map(abs, t))
s = sum(p)
if n & 1 == 0 and len([0 for i in t if i < 0]) & 1:
    s -= 2 * min(p)
print(s)
