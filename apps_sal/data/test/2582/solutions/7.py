n = int(input())
a = list(map(int, input().split()))
dc = {a[i]: i for i in range(n)}
stack = []
mxr = [n] * (n + 1)
mxl = [-1] * (n + 1)
for i, x in enumerate(a):
    if i == 0:
        stack.append(x)
        continue
    while stack and stack[-1] < x:
        y = stack.pop()
        mxr[y] = i
    stack.append(x)
stack = []
for i, x in enumerate(a[::-1]):
    i = n - 1 - i
    if i == n - 1:
        stack.append(x)
        continue
    while stack and stack[-1] < x:
        y = stack.pop()
        mxl[y] = i
    stack.append(x)
ans = 0
for i in range(n, 0, -1):
    idx = dc[i]
    l = mxl[i]
    r = mxr[i]
    if idx - l - 1 > r - idx - 1:
        for j in range(idx + 1, r):
            if l < dc[i - a[j]] < idx:
                ans += 1
    else:
        for j in range(idx - 1, l, -1):
            if idx < dc[i - a[j]] < r:
                ans += 1
print(ans)
