t = int(input())
for i in range(t):
    n = int(input())
    s = str(n)
    ans = (len(s) - 1) * 9
    for j in range(1, 10):
        if int(str(j) * len(s)) <= n:
            ans += 1
        else:
            break
    print(ans)
