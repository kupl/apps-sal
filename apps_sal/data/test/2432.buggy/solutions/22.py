a = int(input())
mult = [32, 1, 4, 8, 2, 16]
out = 0
for (i, c) in enumerate(format(a, '#08b')[2:]):
    if c == '1':
        out += mult[i]
print(out)
