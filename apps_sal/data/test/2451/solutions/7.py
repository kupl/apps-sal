n, h, a, b, k = list(map(int, input(). split()))
for i in range(k):
    t1, f1, t2, f2 = list(map(int, input(). split()))
    if t1 == t2:
        print(abs(f1 - f2))
        continue
    ans = abs(t1 - t2)
    p = 0
    if f1 < a:
        ans += a - f1
        p = a
    elif f1 > b:
        ans += f1 - b
        p = b
    else:
        p = f1
    ans += abs(p - f2)
    print(ans)
