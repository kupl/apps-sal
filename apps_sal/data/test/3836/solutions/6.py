from math import ceil
n, A = int(input()), []
a = b = ab = ab_ = ans = 0
for _ in range(n):
    t, tt = input().split()
    tt = int(tt)
    if t != '11':
        A.append([t, tt])
        if t == '10':
            a += 1
        elif t == '01':
            b += 1
        else:
            ab_ += 1
    else:
        ans += tt
        ab += 1
A.sort(reverse=True, key=lambda x: x[1])
x = y = t = ttt = ab
k, j = a, b
for i in A:
    if i[0] == '10' and (j or ttt):
        ans += i[1]
        t += 1
        x += 1
        if j == 0 and ttt:
            ttt -= 1
            j = 1
        j -= 1
    elif i[0] == '01' and (k or ttt):
        ans += i[1]
        t += 1
        y += 1
        if k == 0 and ttt:
            ttt -= 1
            k = 1
        k -= 1
    elif i[0] == '00' and ttt:
        ans += i[1]
        ttt -= 1
        t += 1
print(ans)
