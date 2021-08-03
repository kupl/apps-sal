t = int(input())
for i in range(t):
    ans = 0
    a = int(input())
    while a >= 4:
        ans += 1
        a -= 2
    if a != 0:
        print(ans + 1)
    else:
        print(ans)
