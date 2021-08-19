(n, m) = [int(i) for i in input().split()]
s = [0] * m
d = [0] * m
c = [0] * m
for i in range(m):
    (s[i], d[i], c[i]) = [int(j) - 1 for j in input().split()]
    c[i] += 1
    if d[i] - s[i] < c[i]:
        print(-1)
        quit()
ans = [0] * n
for i in d:
    ans[i] = m + 1
exam = []
for i in range(n):
    exam.append([])
    for j in range(m):
        if s[j] <= i < d[j]:
            exam[i].append(j)
for i in range(n):
    if ans[i] == 0:
        day_min = n + 1
        for j in exam[i]:
            if d[j] < day_min and c[j] > 0:
                day_min = d[j]
                exam_min = j
        if day_min != n + 1:
            ans[i] = exam_min + 1
            c[exam_min] -= 1
    elif c[d.index(i)] != 0:
        print(-1)
        quit()
for i in range(n):
    if i != n - 1:
        print(ans[i], end=' ')
    else:
        print(ans[i])
