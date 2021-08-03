n, k = list(map(int, input().split()))
a, b, c, d = list(map(int, input().split()))
if n == 4 or k < n + 1:
    print(-1)
    return
extra = 1
while extra == a or extra == b or extra == c or extra == d:
    extra += 1
v = [a, c, extra, d]
k = extra + 1
while k <= n:
    if k != a and k != b and k != c and k != d and k != extra:
        v.append(k)
    k += 1
v.append(b)
print(*v)
u = [c, a, extra] + list(reversed(v[3:]))
print(*u)
