

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))

    for i in range(n):
        a[i] %= 3

    c0 = 0
    c1 = 0
    c2 = 0

    for i in a:
        if(i == 0):
            c0 += 1
        elif(i == 1):
            c1 += 1
        else:
            c2 += 1

    ans = 0

    ans += c0

    now = min(c2, c1)

    ans += now

    c1 -= now
    c2 -= now

    ans += c1 // 3
    ans += c2 // 3

    print(ans)
