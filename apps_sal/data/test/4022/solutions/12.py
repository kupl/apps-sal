from sys import stdin
n = int(stdin.readline())
a = []
max_l = 0
min_r = 10000000000
for i in range(n):
    l, r = map(int, stdin.readline().split())
    a.append((l, r))
    max_l = max(l, max_l)
    min_r = min(r, min_r)
l_ans = 10000000000
li = 0
r_ans = 10000000000
ri = 0
for i in range(n):
    if a[i][0] == max_l:
        if a[i][1] - max_l < l_ans:
            l_ans = a[i][1] - max_l
            li = i
    if a[i][1] == min_r:
        if min_r - a[i][0] < r_ans:
            r_ans = min_r - a[i][0]
            ri = i
max_l = 0
min_r = 10000000000
for i in range(len(a)):
    if i == li:
        continue
    max_l = max(a[i][0], max_l)
    min_r = min(a[i][1], min_r)
ans = min_r - max_l
max_l = 0
min_r = 10000000000
for i in range(len(a)):
    if i == ri:
        continue
    max_l = max(a[i][0], max_l)
    min_r = min(a[i][1], min_r)
ans = max(ans, min_r - max_l)

if ans > 0:
    print(ans)
else:
    print('0')
