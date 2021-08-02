n, m = list(map(int, input().split()))
a = [list(input()) for i in range(n)]
p1 = 0
pp = 0
pm = 0
sm = 0
d = [True] * m
for i in range(m):
    for j in range(n):
        if i == 0 and a[j][i] == '*' and d[i]:
            pp = n - j
            d[i] = False
        elif d[i] and a[j][i] == '*':
            p1 = n - j
            if pp > p1 and pp - p1 > sm:
                sm = pp - p1
            if p1 - pp > pm:
                pm = p1 - pp
            pp = p1
            p1 = n - j
            d[i] = False

print(pm, sm)
