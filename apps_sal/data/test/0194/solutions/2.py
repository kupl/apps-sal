n, a, b = map(int, input().split())

c = 0

ans = 0

for v in map(int, input().split()):
    if v == 1:
        if a:
            a -= 1
        elif b:
            b -= 1
            c += 1
        elif c:
            c -= 1
        else:
            ans += 1
    else:
        if b:
            b -= 1
        else:
            ans += 2

print(ans)
