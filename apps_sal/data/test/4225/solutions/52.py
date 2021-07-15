a, b, c, k = list(map(int, input().split()))
ans = 0
if k > a:
    ans += a
    k -= a
elif k <= a:
    print(k)
    return

if k > b:
    k -= b
elif k <= b:
    print(ans)
    return

print((ans-k))

