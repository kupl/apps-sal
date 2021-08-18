n, a, b = map(int, input().split())
v = list(map(int, input().split()))
fact = [1]
for i in range(1, 51):
    fact.append(i * fact[-1])


def cmb(n, r):
    return fact[n] // (fact[n - r] * fact[r])


v.sort(reverse=True)
print(sum(v[:a]) / a)
cntv, cntr = 0, 0
for i in range(n):
    if i < a:
        if v[i] == v[a - 1]:
            cntv += 1
    else:
        if v[i] == v[a - 1]:
            cntr += 1
if cntv < a:
    print(cmb(cntv + cntr, cntv))
else:
    ans = 0
    for r in range(a, min(b, cntv + cntr) + 1):
        ans += cmb(cntv + cntr, r)
    print(ans)
