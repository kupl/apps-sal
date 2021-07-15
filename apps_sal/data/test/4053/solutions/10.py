n = int(input())
a = [(input(), q) for q in range(2*n-2)]
answer = ['S']*(2*n-2)
a.sort(key=lambda x: (len(x[0]), x))
a1, a = [q[1] for q in a], [q[0] for q in a]
if len(a) == 2:
    print('PS')
else:
    s = [a[-1]+a[0], a[-1]+a[1], a[-2]+a[0], a[-2]+a[1]]
    ans = 0
    for q in range(4):
        d = []
        for q1 in range(1, n):
            d.append(s[q][:q1])
        for q1 in range(n-1, 0, -1):
            d.append(s[q][q1:])
        if sorted(d, key=lambda x: (len(x), x)) == a:
            ans = q
    s = s[ans]
    f = [1]*(2*n-2)
    for q in range(1, n):
        if f[2*q-2] and a[2*q-2] == s[:q]:
            f[2*q-2] = 0
            answer[a1[2*q-2]] = 'P'
        else:
            f[2 * q - 1] = 0
            answer[a1[2 * q - 1]] = 'P'
    print(*answer, sep='')

