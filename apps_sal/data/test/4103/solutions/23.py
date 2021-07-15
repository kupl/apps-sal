n, b, a = list(map(int, input().split()))
line = list(map(int, input().split()))
b1, a1 = b, a
dist = 0
for cell in line:
    if cell == 1:
        if a1 < a and b1 > 0:
            b1 -= 1
            a1 += 1
            dist += 1
        elif a1 > 0:
            a1 -= 1
            dist += 1
        else:
            break
    else:
        if a1 > 0:
            a1 -= 1
            dist += 1
        elif b1 > 0:
            b1 -= 1
            dist += 1
        else:
            break
print(dist)

