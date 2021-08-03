for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(1, 10):
        s = ''
        for j in range(10):
            s += str(i)
            if int(s) <= n:
                ans += 1
    print(ans)
