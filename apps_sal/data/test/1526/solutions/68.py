a, b, c = map(int, input().split())
ans = 0
while 1:
    if a == b and b == c:
        print(ans)
        break
    ans += 1
    if a == min(a, b, c):
        a += 1
        if a == min(a, b, c):
            a += 1
        elif b == min(a, b, c):
            b += 1
        else:
            c += 1
    elif b == min(a, b, c):
        b += 1
        if a == min(a, b, c):
            a += 1
        elif b == min(a, b, c):
            b += 1
        else:
            c += 1
    else:
        c += 1
        if a == min(a, b, c):
            a += 1
        elif b == min(a, b, c):
            b += 1
        else:
            c += 1
