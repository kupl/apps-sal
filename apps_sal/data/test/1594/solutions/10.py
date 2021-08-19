(n, m) = list(map(int, input().split()))
s = [0]
k = 0
l = 0
for i in range(n):
    (c, t) = list(map(int, input().split()))
    s.append(s[i] + c * t)
ara = [int(x) for x in input().split()]
for j in range(m):
    while ara[j] > s[l]:
        l += 1
    print(l)
