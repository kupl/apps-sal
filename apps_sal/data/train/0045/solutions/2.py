tests = int(input())
for test in range(tests):
    n = int(input())
    ans = 0
    s = 0
    for i in range(1, 31):
        d = 2 ** i - 1
        r = d * (d + 1) // 2
        if s + r <= n:
            ans += 1
            s += r
        else:
            break
    print(ans)
        

