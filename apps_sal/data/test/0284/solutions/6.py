import sys

a, b, c = 1234567, 123456, 1234
n = int(input())
for aq in range(int(n // a) + 3):
    nn = n - a * aq
    if nn < 0: break
    for bq in range(int(nn // b) + 3):
        nnn = nn - b * bq
        if nnn < 0: continue
        if nnn % c == 0:
            print("YES")
            return
print("NO")
