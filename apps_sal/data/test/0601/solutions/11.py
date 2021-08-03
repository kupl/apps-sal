t = int(input())
while t:
    t += -1
    p, f = map(int, input().split())
    cnts, cntw = map(int, input().split())
    s, w = map(int, input().split())
    if s > w:
        s, w = w, s
        cnts, cntw = cntw, cnts
    ans = 0
    for i in range(cnts + 1):
        if i * s > p:
            break
        t1 = p - i * s
        t2 = min(t1 // w, cntw)
        t3 = cnts - i
        t4 = cntw - t2
        t5 = min(f // s, t3)
        t6 = f - t5 * s
        t7 = min(t6 // w, t4)
        ans = max(ans, i + t2 + t5 + t7)
    print(ans)
