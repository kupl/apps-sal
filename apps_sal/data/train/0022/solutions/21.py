def f(x):
    s = str(x)
    mn = 12
    mx = 0
    for i in s:
        mx = max(mx, int(i))
        mn = min(mn, int(i))
    return mn * mx


for _ in range(int(input())):
    (a, k) = list(map(int, input().split()))
    k -= 1
    prev = -1
    while k > 0:
        if prev == a:
            break
        prev = a
        a += f(a)
        k -= 1
    print(a)
