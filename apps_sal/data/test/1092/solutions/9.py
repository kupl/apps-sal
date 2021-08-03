def fac(n):
    if n == 0:
        return 1
    mul = 1
    for i in range(2, n + 1):
        mul *= i
    return mul


n, m = (int(t) for t in input().split(' '))
gen = (int(t) for t in input().split(' '))
v = []
for i in gen:
    v.append(i)
v.sort()
ans = fac(n - m)
# print(type(ans))
ans //= fac(v[0] - 1)
for i in range(1, len(v)):
    #    print('#')
    ans //= fac(v[i] - v[i - 1] - 1)
    if v[i] - v[i - 1] - 1 != 0:
        ans *= 2**(v[i] - v[i - 1] - 2)
ans //= fac(n - v[len(v) - 1])
print('%d' % (ans % (int(1e9) + 7)))
