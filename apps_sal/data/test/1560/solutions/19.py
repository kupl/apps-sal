n = int(input())
ch = input()
r1, r2, b1, b2 = 0, 0, 0, 0
for i in range(n):
    if (i % 2 == 0):
        if (ch[i] != 'r'):
            r1 += 1
        if (ch[i] != 'b'):
            b2 += 1

    if (i % 2 != 0):
        if (ch[i] == 'r'):
            b1 += 1
        if (ch[i] == 'b'):
            r2 += 1

print(min(max(r1, b1), max(r2, b2)))
