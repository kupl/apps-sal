n, a, b = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
part = 0
ans = 0
for i in t:
    if i == 1:
        if a:
            a -= 1
        elif b:
            b -= 1
            part += 1
        elif part:
            part -= 1
        else:
            ans += 1
    else:
        if b:
            b -= 1
        else:
            ans += 2
print(ans)

