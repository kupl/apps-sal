(n, a, b) = list(map(int, input().split()))
po = 0
ans = 0
L = list(map(int, input().split()))
for i in L:
    if i == 1:
        if a > 0:
            a -= 1
        elif b > 0:
            b -= 1
            po += 1
        elif po > 0:
            po -= 1
        else:
            ans += 1
    elif b > 0:
        b -= 1
    else:
        ans += 2
print(ans)
