n = int(input())
w = [0] * (n)
h = [0] * (n)
for i in range(n):
    w[i], h[i] = map(int, input().split())
s = sum(w)
temp = sorted(h)
m1, m2 = temp[-1], temp[-2]
for i in range(n):
    a = s - w[i]
    b = m1
    if h[i] == m1:
        b = m2
    print(a*b, end=' ')
