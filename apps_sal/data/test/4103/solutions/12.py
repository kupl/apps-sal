(n, b, a) = list(map(int, input().split()))
s = list(map(int, input().split()))
(b1, a1) = (b, a)
k = 0
for c in s:
    if a1 == 0 and b1 == 0:
        break
    if c == 0:
        if a1 > 0:
            a1 -= 1
        elif b1 > 0:
            b1 -= 1
        else:
            break
    elif a1 != a:
        if b1 > 0:
            b1 -= 1
            a1 += 1
        elif a1 > 0:
            a1 -= 1
        else:
            break
    else:
        a1 -= 1
    k += 1
print(k)
