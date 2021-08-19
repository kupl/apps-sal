n = int(input())
u = list(map(int, input().split()))
i1 = 0
i2 = n - 1
ans = []
m = 0
p = []
while 1 == 1:
    m1 = min(u[i1], u[i2])
    m2 = max(u[i1], u[i2])
    if m > m2:
        break
    if m > m1:
        p.append(m2)
        m = m2
        if u[i1] > u[i2]:
            i1 += 1
            ans.append('L')
        else:
            i2 -= 1
            ans.append('R')
    else:
        p.append(m1)
        m = m1
        if u[i1] < u[i2]:
            i1 += 1
            ans.append('L')
        else:
            i2 -= 1
            ans.append('R')
    if i1 > i2:
        break
print(len(ans))
print(''.join(ans))
