n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
s = 0
c = 0
while True:
    c = 0
    s = 0
    for i in a:
        if i <= t:
            t -= i
            s += i
            c += 1
    if c == 0:
        break
    ans += c
    if s <= t:
        ans += c * (t // s)
        t %= s
print(ans)
