n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
c = [n] * n
for i in range(n):
    c[i] -= (r[i] + l[i])
for i in range(n):
    m = 0
    for j in range(0, i):
        if c[j] > c[i]:
            m += 1
    if m != l[i]:
        print('NO'); return
for i in range(n):
    m = 0
    for j in range(i + 1, n):
        if c[j] > c[i]:
            m += 1
    if m != r[i]:
        print('NO'); return
print('YES')
print(*(c))
