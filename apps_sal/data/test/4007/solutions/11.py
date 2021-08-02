n = int(input())
l = list(map(int, input().split()))
new = [-1] * n
for i in l:
    if i != 0:
        new[i - 1] = 0
d = []
for i in range(n):
    if new[i] == -1:
        d.append(i + 1)
loc = 0
ans = []
index = []
flag = 0
for i in range(n):
    if l[i] != 0:
        ans.append(l[i])
    else:
        if d[loc] != i + 1 and flag == 0:
            ans.append(d[loc])
            if len(index) == 0:
                index.append(i)
        else:
            if len(index) != 0:
                ans.append(d[loc])
                ans[-1], ans[index[-1]] = ans[index[-1]], ans[-1]
                flag = 0
            else:
                flag = 1
                ans.append(d[loc])
                if len(index) == 0:
                    index.append(i)
        loc += 1
print(*ans)
