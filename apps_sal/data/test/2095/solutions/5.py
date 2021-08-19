n = int(input())
a = []
c = 0
ans = []
for i in range(n):
    t = list(map(int, input().split()))
    a.append(t)
num = 0
for i in a:
    if not 1 in i and (not 3 in i):
        c += 1
        ans.append(num + 1)
    num += 1
print(c)
for i in range(c - 1):
    print(ans[i], end=' ')
if c:
    print(ans[c - 1])
