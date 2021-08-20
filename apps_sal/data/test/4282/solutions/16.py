n = int(input())
a = [[0, 0]]
ans = [1]
for i in range(n):
    a.append([int(x) for x in input().split()])
options = a[1]
ans.append(options[0])
ans.append(options[1])
if ans[-1] not in a[ans[-2]]:
    (ans[1], ans[2]) = (ans[2], ans[1])
for i in range(1, n - 1):
    options = a[ans[i]]
    idx = options.index(ans[-1])
    rem = options[1 - idx]
    ans.append(rem)
print(*ans[:-1])
