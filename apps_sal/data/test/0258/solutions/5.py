def f(q1, q2, k1, k2):
    res1 = res2 = 0
    res1 += (q1 + 1) // 2 * k1
    res1 += q1 // 2 * k2
    res2 += q2 // 2 * k2
    res2 += (q2 + 1) // 2 * k1
    return [res1, res2]


n = int(input())
s = input()
sum_l = sum_r = 0
ql = qr = 0
for i in range(n // 2):
    if s[i] == '?':
        ql += 1
    else:
        sum_l += int(s[i])
for i in range(n // 2, n):
    if s[i] == '?':
        qr += 1
    else:
        sum_r += int(s[i])
mn = float('inf')
mx = float('inf')
kek = [f(ql, qr, 0, 9), f(ql, qr, 9, 0), f(qr, ql, 9, 0)[::-1], f(qr, ql, 0, 9)[::-1]]
lol = []
for x in kek:
    lol.append(x[0] + sum_l - x[1] - sum_r)
lol.sort()
if lol[0] <= 0 <= lol[-1]:
    print('Bicarp')
else:
    print('Monocarp')
