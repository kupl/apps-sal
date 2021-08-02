s = input().split()
n, k = int(s[0]), int(s[1])
s = input()

ans = 0

k1 = k
i1 = -1
i2 = 0
while i1 < n - 1:
    i1 += 1
    if s[i1] == 'b':
        if k1 > 0:
            k1 -= 1
        else:
            while s[i2] != 'b':
                i2 += 1
            i2 += 1

    if ans < i1 - i2:
        ans = i1 - i2

k1 = k
i1 = -1
i2 = 0
while i1 < n - 1:
    i1 += 1
    if s[i1] == 'a':
        if k1 > 0:
            k1 -= 1
        else:
            while s[i2] != 'a':
                i2 += 1
            i2 += 1
    if ans < i1 - i2:
        ans = i1 - i2

print(ans + 1)
