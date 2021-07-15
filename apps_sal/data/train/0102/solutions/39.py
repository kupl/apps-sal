t = int(input())
for i in range(t):
    n = int(input())
    j = 1
    while int("9" * j) <= n:
        j += 1
    ans = 9 * (j - 1)
    for k in range(1, 9):
        if int(str(k) * j) <= n:
            ans += 1
        else:
            break
    print(ans)

