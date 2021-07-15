H = int(input())

ans = 1
if H != 1:
    h = H
    for i in range(1, 40):
        if int(h/2) >= 2:
#            print(i, ans, h, 'a')
            ans += 2**i
            h = int(h/2)
        else:
#            print(i, ans, h, 'b')
            ans += 2**i
            break

print(ans)
