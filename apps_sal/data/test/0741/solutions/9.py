n, M = map(int, input().split(' '))
a = input().split(' ')
for i in range(n):
    a[i] = int(a[i])
a.insert(0, 0)
a.append(M)
p = 0
o = 0
for i in range(1, n + 2):
    if i%2 == 1:
        p += a[i] - a[i-1]
    else:
        o += a[i] - a[i-1]
raz = p
ind = -1
a_p = 0
a_o = 0
for i in range(1, n + 2):
    if i%2 == 0:
        if a[i] - a[i-1] != 1:
            if a_p - 1 + o > raz:
                raz = a_p-1+o
        o -= a[i]-a[i-1]
        a_o += a[i]-a[i-1]
    else:
        if a[i] - a[i-1] != 1:
            if a_p + a[i] - a[i-1] - 1 + o > raz:
                raz = a_p+a[i]-a[i-1]-1+o
        p -= a[i]-a[i-1]
        a_p += a[i]-a[i-1]
print(raz)
