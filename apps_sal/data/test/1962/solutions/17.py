(n, k, l) = list(map(int, input().split()))
a = list(map(int, input().split()))
a0 = min(a)
v = []
for ai in a:
    if ai <= a0 + l:
        v.append(ai)
v = list(sorted(v))
m = len(v)
if m < n:
    ans = 0
else:
    ans = 0
    a = n
    b = m
    i = 0
    j = 0
    for vi in v:
        if i == 0:
            ans += vi
        if i == k - 1 or a == b:
            i = 0
            j += 1
            a -= 1
        else:
            i += 1
        b -= 1
print(ans)
