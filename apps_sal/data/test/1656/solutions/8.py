s = input()
w, wo, wow = 0, 0, 0
last = None
for c in s:
    if c == 'v' and last == 'v':
        w += 1
        wow += wo
    elif c == 'o':
        wo += w
    last = c

print(wow)
