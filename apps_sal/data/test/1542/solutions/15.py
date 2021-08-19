import sys
line = sys.stdin.readlines()
n = int(line[0])
x = list(map(int, line[1].split()))
x.sort()
q = int(line[2])
y = []
for i in range(q):
    y.append((int(line[i + 3]), i))
y.sort()
ans = []
j = 0
cnt = 0
for (m, i) in y:
    while j < n and m >= x[j]:
        cnt += 1
        j += 1
    ans.append((i, cnt))
ans.sort()
for (i, a) in ans:
    print(a)
