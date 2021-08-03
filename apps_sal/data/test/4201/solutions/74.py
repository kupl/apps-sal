h, w, k, = map(int, input().split())

c = [0] * h
for i in range(h):
    c[i] = input()

y = 0

for i in range(2 ** (h + w)):
    x = 0
    a = [0] * (h + w)
    for j in range(h + w):
        if (i // (2 ** j)) % 2 == 1:
            a[j] = 1

    for j in range(h):
        if a[j] == 0:
            for l in range(w):
                if a[h + l] == 0:
                    if c[j][l] == '#':
                        x += 1

    if x == k:
        y += 1

print(y)
