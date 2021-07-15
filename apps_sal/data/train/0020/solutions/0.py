q = int(input())
for _ in range(q):
    n, m = list(map(int, input().split()))
    info = [list(map(int, input().split())) for i in range(n)]
    info = sorted(info)
    now =(m, m)
    time = 0
    flag = True
    for i in range(n):
        t, l, h = info[i]
        l_now = now[0] - (t - time)
        h_now = now[1] + (t - time)
        time = t
        if h < l_now or h_now < l:
            flag = False
        else:
            l_now = max(l_now, l)
            h_now = min(h_now, h)
            now = (l_now, h_now)
    if flag:
        print("YES")
    else:
        print("NO")
