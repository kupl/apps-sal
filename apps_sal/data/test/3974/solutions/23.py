s = input()

d, f, r = 0, 0, 0
for c in s:
    if c == "-":
        f += 1
        if d >= 1:
            d -= 1
        else:
            r += 1
    elif c == "+":
        d += 1
        if f >= 1:
            f -= 1
        else:
            r += 1

print(r)
