t = eval(input())
for test in range(t):
    l = [int(i) for i in input().split()]

    a = l[0]
    b = l[1]
    c = l[2]
    d = l[3]
    ans = 0

    for i in range(a, b + 1):
        if i >= c and i <= d:
            ans += (d - i)
        elif i < c:
            ans += (d - c + 1)
        # print ans

    print(ans)
