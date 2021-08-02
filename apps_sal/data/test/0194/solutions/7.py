n, a, b = [int(s) for s in input().split()]
t = [int(s) for s in input().split()]
ans, c = 0, 0
for i in range(n):
    if t[i] == 1:
        if a > 0:
            a -= 1
        elif b > 0:
            b -= 1
            c += 1
        elif c > 0:
            c -= 1
        else:
            ans += 1
    else:
        if b > 0:
            b -= 1
        else:
            ans += 2
print(ans)
