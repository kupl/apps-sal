(n, a, b, k) = list(map(int, input().split()))
ar = list(map(int, input().split()))
kek = []
ans = 0
for elem in ar:
    x = elem % (a + b)
    if x == 0 or x > a:
        if x == 0:
            x = a + b
        kek.append((x + a - 1) // a - 1)
    else:
        ans += 1
kek.sort()
i = 0
while i < len(kek) and k > 0:
    if k - kek[i] >= 0:
        k -= kek[i]
        i += 1
        ans += 1
    else:
        break
print(ans)
