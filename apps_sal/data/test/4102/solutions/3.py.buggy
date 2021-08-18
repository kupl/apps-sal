import sys

s = input()
pairs = [(3, 3), (4, 6), (5, 9), (6, 4), (7, 7), (8, 0), (9, 5), (0, 8)]

for l in range(len(s) // 2 + 1):
    r = len(s) - l - 1
    if l == r and int(s[l]) not in [3, 7]:
        print("No")
        return
    elif (int(s[l]), int(s[r])) not in pairs:
        print("No")
        return

print("Yes")
