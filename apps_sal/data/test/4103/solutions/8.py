(n, a, b) = list(map(int, input().split()))
mab = b
l = list(map(int, input().split()))
ans = 0
for x in l:
    if x == 0:
        if b > 0:
            b -= 1
            ans += 1
        elif a > 0:
            a -= 1
            ans += 1
        else:
            break
    elif mab == b:
        b -= 1
        ans += 1
    elif a > 0:
        a -= 1
        b += 1
        ans += 1
    elif b > 0:
        ans += 1
        b -= 1
    else:
        break
print(ans)
