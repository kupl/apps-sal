

from sys import stdin

inp = stdin.readline

n, m, d = list(map(int, inp().split()))
a = [(int(minute), index) for index, minute in enumerate(inp().split())]
ans = [0] * n

a.sort()
ans[a[0][1]] = 1
max_cur_day = 1
j = 0
count = 1

for i in range(1, n):
    if a[i][0] - a[j][0] > d:
        ans[a[i][1]] = ans[a[j][1]]
        j += 1
    else:
        count += 1
        ans[a[i][1]] = count

print(count)
print(*ans)
