n = int(input())

used = 0
h = 0
s = 1
while used <= n:
    used += s
    h += 1
    s += h + 1
print(h - 1)

