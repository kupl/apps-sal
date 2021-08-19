n = int(input())
l = list(map(int, input().split()))
x = [4, 8, 15, 16, 23, 42]
d = {}
for i in x:
    d[i] = 0
count = 0
for i in range(n):
    if l[i] == 4:
        d[4] += 1
    elif l[i] == 8:
        if d[4] == 0:
            count += 1
        else:
            d[4] -= 1
            d[8] += 1
    elif l[i] == 15:
        if d[8] == 0:
            count += 1
        else:
            d[8] -= 1
            d[15] += 1
    elif l[i] == 16:
        if d[15] == 0:
            count += 1
        else:
            d[15] -= 1
            d[16] += 1
    elif l[i] == 23:
        if d[16] == 0:
            count += 1
        else:
            d[16] -= 1
            d[23] += 1
    elif d[23] == 0:
        count += 1
    else:
        d[23] -= 1
        d[42] += 1
count += d[4] + 2 * d[8] + 3 * d[15] + 4 * d[16] + 5 * d[23]
print(count)
