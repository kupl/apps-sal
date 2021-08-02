n, r, avg = list(map(int, input().split()))
exams, need, ans = [], avg * n, 0
for x in range(n):
    a, b = list(map(int, input().split()))
    exams.append([b, a])
    need -= a
exams.sort()
i = 0
while need > 0 and i < n:
    ans += exams[i][0] * min(r - exams[i][1], need)
    need -= min(r - exams[i][1], need)
    i += 1
print(ans)
