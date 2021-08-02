a, b, k = map(int, input().split())

total = a + b
if total <= k:
    ans = [0, 0]
else:
    if a <= k:
        k -= a
        a = 0
        b -= k
        ans = [a, b]
    else:
        a -= k
        ans = [a, b]

print(*ans)
