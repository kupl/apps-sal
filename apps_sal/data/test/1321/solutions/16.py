n = int(input())
w = [[] for i in range(n)]
h = [[] for i in range(n)]
h1 = [[] for i in range(n)]
sum = 0
for i in range(n):
    (wi, hi) = map(int, input().split())
    w[i] = wi
    h[i] = hi
    h1[i] = hi
    sum += wi
m1 = max(h)
h1.remove(m1)
m2 = max(h1)
for i in range(n):
    s1 = sum - w[i]
    if h[i] == m1:
        s2 = m2
    else:
        s2 = m1
    print(s1 * s2, end=' ')
