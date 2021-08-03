import bisect
n, k, c = map(int, input().split())
s = input()

lst = []
for i in range(n):
    if s[i] == 'o':
        lst.append(i + 1)

x, y = [], []
for i in range(len(lst)):
    if i == 0:
        x.append(lst[i])
    else:
        if lst[i] - x[-1] > c:
            x.append(lst[i])
    if len(x) == k:
        break

for i in range(len(lst))[::-1]:
    if i == len(lst) - 1:
        y.append(lst[i])
    else:
        if y[-1] - lst[i] > c:
            y.append(lst[i])
    if len(y) == k:
        break

x.sort()
y.sort()

ans = []
for i in range(k):
    if x[i] == y[i]:
        ans.append(x[i])
for a in ans:
    print(a)
