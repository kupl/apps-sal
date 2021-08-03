n, z = map(int, input().split())
b = []
s = []
for i in range(n):
    h = input().split()
    if h[0] == "B":
        bb = True
        for j in range(len(b)):
            (x, y) = b[j]
            if x == int(h[1]):
                b[j] = (x, y + int(h[2]))
                bb = False
        if bb:
            b += [(int(h[1]), int(h[2]))]
    else:
        bb = True
        for j in range(len(s)):
            (x, y) = s[j]
            if x == int(h[1]):
                s[j] = (x, y + int(h[2]))
                bb = False
        if bb:
            s += [(int(h[1]), int(h[2]))]

b = sorted(b, key=lambda colonnes: colonnes[0])
s = sorted(s, key=lambda colonnes: colonnes[0])

i = 0
h = 0
while h < z and len(s) - 1 - i >= 0:
    if len(s) - 1 - i < z:
        print("S", s[len(s) - 1 - i][0], s[len(s) - 1 - i][1])
        h += 1
    i += 1
for i in range(z):
    if len(b) - 1 - i >= 0:
        print("B", b[len(b) - 1 - i][0], b[len(b) - 1 - i][1])
