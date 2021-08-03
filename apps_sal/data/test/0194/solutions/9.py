n, a, b = list(map(int, input().split()))
L = list(map(int, input().split()))
b1 = 0
ans = 0
for i in L:
    if i == 1:
        if a > 0:
            a -= 1
        elif b > 0:
            b -= 1
            b1 += 1
        elif b1 > 0:
            b1 -= 1
        else:
            ans += 1
    else:
        if b > 0:
            b -= 1
        else:
            ans += 2
print(ans)
