import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline
points = read().strip()
lst = [[points[0], 1]]
for p in points[1:]:
    if p == lst[-1][0]:
        lst[-1][1] += 1
    else:
        lst += [[p, 1]]
ans = 0
while len(lst) > 1:
    ans += 1
    tmp = []
    if lst[0][1] > 1:
        tmp.append([lst[0][0], lst[0][1] - 1])
    for i in lst[1:-1]:
        if i[1] > 2:
            if len(tmp) == 0 or tmp[-1][0] != i[0]:
                tmp.append([i[0], i[1] - 2])
            else:
                tmp[-1][1] += i[1] - 2
    if lst[-1][1] > 1:
        if len(tmp) == 0 or lst[-1][0] != tmp[-1][0]:
            tmp.append([lst[-1][0], lst[-1][1] - 1])
        else:
            tmp[-1][1] += lst[-1][1] - 1
    lst = tmp
print(ans)
