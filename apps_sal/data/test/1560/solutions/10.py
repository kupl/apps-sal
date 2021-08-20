n = int(input())
s = input()
ab = 0
ar = 0
ab1 = 0
ar1 = 0
if s[0] == 'b':
    for i in range(n):
        if (i + 1) % 2 == 1:
            if s[i] != 'b':
                ab += 1
        elif s[i] != 'r':
            ar += 1
    for i in range(n):
        if (i + 1) % 2 == 1:
            if s[i] != 'r':
                ar1 += 1
        elif s[i] != 'b':
            ab1 += 1
else:
    for i in range(n):
        if (i + 1) % 2 == 1:
            if s[i] != 'r':
                ab += 1
        elif s[i] != 'b':
            ar += 1
    for i in range(n):
        if (i + 1) % 2 == 1:
            if s[i] != 'b':
                ab1 += 1
        elif s[i] != 'r':
            ar1 += 1
if max(ab1, ar1) > max(ab, ar):
    print(max(ab, ar))
else:
    print(max(ab1, ar1))
