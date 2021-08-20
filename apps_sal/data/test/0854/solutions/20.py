(n, T) = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
while True:
    t = m = 0
    for x in a:
        if T - t >= x:
            t += x
            m += 1
    if not m:
        break
    ans += T // t * m
    T %= t
print(ans)
