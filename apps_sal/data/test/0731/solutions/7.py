w, m, k = map(int, input().split())
ans = 0
while w >= len(str(m)) * k:
    ans += min(w // (k * len(str(m))), 10**len(str(m)) - m)
    w1 = w
    m1 = m
    m += min(w1 // (k * len(str(m1))), 10**len(str(m1)) - m1)
    w -= k * len(str(m1)) * min(w1 // (k * len(str(m1))), 10**len(str(m1)) - m1)
    # print(w,m,ans)
print(ans)
