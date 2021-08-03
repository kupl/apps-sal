n, m = input().split()
d = {0: 1}
r = s = 0
for i in input().split():
    s += int(i)
    s %= int(m)
    x = d.get(s, 0)
    r += x
    d[s] = x + 1
print(r)
