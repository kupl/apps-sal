for i in range(int(input())):
    n = int(input())
    ans = 0
    for k in range(1, 11):
        for j in range(1, 10):
            s = str(j) * k
            if int(s) <= n:
                ans += 1
    print(ans)
