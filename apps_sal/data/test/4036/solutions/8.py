def mp():
    return map(int, input().split())


n, k = mp()
a = [i for i in range(1, k + 1)]
s = (1 + k) * k // 2

p = [0] * k
pp = 0

i = 0
while i < k and s < n:
    #print(n - s), (k - i), (n - s) // (k - i)
    q = (n - s) // (k - i)
    if i == 0 or a[i] + q <= 2 * a[i - 1] + pp:
        p[i] = q
        pp += q
        s += q * (k - i)
    i += 1

if s == n:
    print('YES')
    q = 0
    for i in range(k):
        q += p[i]
        print(a[i] + q, end=' ')
else:
    print('NO')
