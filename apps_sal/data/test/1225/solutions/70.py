H = int(input())

ans = 1
if H != 1:
    h = H
    for i in range(1, 40):
        if int(h / 2) >= 2:
            ans += 2**i
            h = int(h / 2)
        else:
            ans += 2**i
            break

print(ans)
