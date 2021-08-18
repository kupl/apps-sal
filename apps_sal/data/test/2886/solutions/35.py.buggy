import sys
s = input()
for i, (x, y) in enumerate(zip(s, s[1:])):
    if x == y:
        print(i + 1, i + 2)
        return
if len(s) <= 2:
    print(-1, -1)
    return
for i, (x, y, z) in enumerate(zip(s, s[1:], s[2:])):
    if x == z:
        print(i + 1, i + 3)
        return
print(-1, -1)
