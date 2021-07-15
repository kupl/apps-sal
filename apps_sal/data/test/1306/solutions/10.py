f = lambda: map(int, input().split())
n, h = f()
s, i = 1, 0
for j in f():
    j = h - j
    if j < 0 or abs(j - i) > 1: print(0);return
    if j <= i: s = s * (j + 1) % 1000000007
    i = j
print(0 if i > 1 else s)
