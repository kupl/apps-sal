(n, k) = map(int, input().split())
a = list(map(int, input().split()))
p = [[0, 0, 0] for i in range(k)]
j = 0
m = 0
ans = [0] * n
flag = True
while flag:
    flag = False
    t = 0
    for i in range(k):
        p[i][0] += 1
        if p[i][0] == int(m / n * 100 + 0.5):
            ans[p[i][2]] = 1
        if p[i][0] >= p[i][1]:
            if p[i][1] != 0:
                t += 1
            if j >= n:
                p[i] = [0, 0, 0]
            else:
                p[i][0] = 0
                p[i][1] = a[j]
                p[i][2] = j
                j += 1
        if p[i][1] != 0:
            flag = True
    m += t
print(sum(ans))
