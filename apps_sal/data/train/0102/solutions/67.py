t = int(input())
for q in range(t):
    n = input()
    k = len(n)
    ans = 9 * (k - 1)
    a1 = n[0]
    v = ''
    for i in range(k):
        v += a1
    n = int(n)
    v = int(v)
    if v <= n:
        ans += int(a1)
    else:
        ans += int(a1) - 1
    print(ans)
