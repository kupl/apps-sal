t = int(input())
for _ in range(t):
    p, f = map(int, input().split())
    cs, cw = map(int, input().split())
    s, w = map(int, input().split())
    if s > w:
        cs, cw = cw, cs
        s, w = w, s
    if p // s + f // s <= cs:
        print(p // s + f // s)
    else:
        ans = 0
        for i in range(cs + 1):
            if s * i <= p and s * (cs - i) <= f:
                a = p - s * i
                b = f - s * (cs - i)
                ans = max(ans, cs + min(cw, a // w + b // w))
        print(ans)
