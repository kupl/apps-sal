n = int(input())
l = [-2] * (n * 2 + 1)
l[n], r = -1, 0
for i, c in enumerate(input()):
    n += ord(c) * 2 - 97
    if l[n] == -2:
        l[n] = i
    else:
        i -= l[n]
        if r < i:
            r = i
print(r)
