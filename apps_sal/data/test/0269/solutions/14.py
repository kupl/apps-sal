colors = set("RGBY".split())
s = input()
r, g, b, y = 0, 0, 0, 0
R, G, B, Y = -1, -1, -1, -1

for i in range(len(s)):
    if s[i] == "R":
        R = i % 4
    elif s[i] == "G":
        G = i % 4
    elif s[i] == "B":
        B = i % 4
    else:
        Y = i % 4

for i in range(len(s)):
    if s[i] == "!":
        if i % 4 == R:
            r += 1
        elif i % 4 == G:
            g += 1
        elif i % 4 == B:
            b += 1
        else:
            y += 1
print(r, b, y, g)

