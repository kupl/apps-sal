n = int(input())
h = tuple(map(int, str.split(input())))
hm = [0] * (n)

ch = 0
for i, x in enumerate(reversed(h)):

    hm[i] = max(0, ch - x + 1)
    ch = max(ch, x)

print(str.join(" ", list(map(str, reversed(hm)))))
