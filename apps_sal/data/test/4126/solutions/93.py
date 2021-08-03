s = list(input())
b = 0
if len(s) % 2 == 1:
    for a in range(int((len(s) - 1) / 2)):
        if s[a] != s[len(s) - a - 1] and b == 0:
            b = 1
else:
    b = 1
if b == 0:
    for c in range(int((len(s) - 1) / 4 + 1)):
        if s[c] == s[int((len(s) - 1) / 2 - c - 1)] == s[int((len(s) + 1) / 2 + c)] == s[len(s) - c - 1] and b == 0:
            b = 0
        else:
            b = 1
if b == 0:
    print("Yes")
elif b == 1:
    print("No")
