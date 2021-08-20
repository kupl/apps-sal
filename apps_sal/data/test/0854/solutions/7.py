(n, t) = map(int, input().split())
a = list(map(int, input().split()))
suma = sum(a)
a = {i: a[i] for i in range(n)}
ans = 0
c = 0
left = n
while suma != 0:
    ans += t // suma * left
    t = t % suma
    while suma > t:
        if c in a:
            if t < a[c]:
                suma -= a[c]
                left -= 1
                del a[c]
            else:
                t -= a[c]
                ans += 1
        c = (c + 1) % n
print(ans)
