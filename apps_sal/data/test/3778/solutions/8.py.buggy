import sys
n = int(input())
a = list(map(int, input().split()))
height = n
ans = []
last3 = -1
fail = 0
used = -1
for i in range(n):
    if a[i] == 3:
        if height == n:
            ans.append((n - height + 1, i + 1))
            height -= 1
        else:
            ans.append((n + 1 - (height + 1), i + 1))
            ans.append((n + 1 - height, i + 1))
            height -= 1
        last3 = i
if last3 == n - 1:
    print(-1)
    return
if last3 > -1:
    flag = 0
    for i in range(last3, n):
        if a[i] == 2:
            flag = 1
            ans.append((n + 1 - (height + 1), i + 1))
            height -= 1
            break
    if flag == 0:
        flag2 = 0
        for i in range(last3, n):
            if a[i] == 1:
                ans.append((n + 1 - (height + 1), i + 1))
                height -= 1
                flag2 = 1
                used = i
                break
        if flag2 == 0:
            print(-1)
            return
ones = []
if used == -1:
    height -= 1
for i in range(n - 1, -1, -1):
    if a[i] == 1 and i != used:
        ones.append(i)
    if a[i] == 2:
        if len(ones) == 0:
            print(-1)
            return
        k = ones.pop()
        ans.append((n + 1 - (height + 1), i + 1))
        ans.append((n + 1 - (height + 1), k + 1))
        height -= 1
if used > -1:
    ones.append(used)
for i in ones:
    ans.append((n + 1 - (height + 1), i + 1))
    height -= 1
print(len(ans))
for x, y in ans:
    print(x, y)
