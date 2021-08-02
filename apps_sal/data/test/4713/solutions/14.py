input(); x, r = 0, 0
for i in input():
    if i == 'I': x += 1
    else: x -= 1
    r = max(r, x)
print(r)
