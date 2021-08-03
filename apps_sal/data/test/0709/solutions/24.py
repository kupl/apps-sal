a = int(input())
if a == 1:
    print(1)
else:
    ans = 1
    while a != 1:
        if a % 2:
            ans += 1
            a -= 1
        a /= 2
    print(ans)
