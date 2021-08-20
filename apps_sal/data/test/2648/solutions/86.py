from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i in range(N):
    if d[A[i]] == 0:
        d[A[i]] = 1
    else:
        d[A[i]] += 1
sorted_d = sorted(list(d.items()), key=lambda x: x[1], reverse=True)
fix_d = []
for i in range(len(sorted_d)):
    if sorted_d[i][1] >= 3:
        if sorted_d[i][1] % 2 == 0:
            fix_d.append([sorted_d[i][0], 2])
        else:
            fix_d.append([sorted_d[i][0], 1])
    else:
        fix_d.append([sorted_d[i][0], sorted_d[i][1]])
fix_d.sort(key=lambda x: x[1], reverse=True)
count = 0
for i in range(len(fix_d)):
    if fix_d[i][1] == 2:
        count += 1
if count % 2 == 0:
    print(len(fix_d))
else:
    print(len(fix_d) - 1)
