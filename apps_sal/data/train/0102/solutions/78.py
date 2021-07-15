t = int(input())
for i in range(t):
    n = int(input())
    r = len(str(n))
    cnt = 0
    cnt += (r - 1) * 9
    x = int(str(n)[0])
    if int(str(x) * r) <= n:
        cnt += x
    else:
        cnt += x - 1
    print(cnt)
