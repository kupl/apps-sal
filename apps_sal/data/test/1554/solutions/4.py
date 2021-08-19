n = int(input())
lst = list(map(int, input().split()))
ans = []
l = 0
r = -1
s = set()
for i in range(n):
    if lst[i] in s:
        ans.append([l + 1, i + 1])
        s = set()
        l = i + 1
        r = i + 1
    else:
        s.add(lst[i])
if r != n and r != -1:
    ans[-1][1] = n
if r == -1:
    print(-1)
else:
    print(len(ans))
    for i in ans:
        print(*i)
