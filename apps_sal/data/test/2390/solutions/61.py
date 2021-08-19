(n, c) = map(int, input().split())
x = []
v = []
rightvalue = []
temp = 0
for i in range(n):
    (xi, vi) = map(int, input().split())
    x.append(xi)
    v.append(vi)
    temp += vi
    rightvalue.append(temp - xi)
rightmaxdouble = []
currentmax = 0
for i in range(n):
    if currentmax < rightvalue[i] - x[i]:
        currentmax = rightvalue[i] - x[i]
    rightmaxdouble.append(currentmax)
leftvalue = []
temp = 0
for i in range(n):
    temp += v[n - 1 - i]
    leftvalue.append(temp - (c - x[n - 1 - i]))
leftmaxdouble = []
currentmax = 0
for i in range(n):
    if currentmax < leftvalue[i] - (c - x[n - 1 - i]):
        currentmax = leftvalue[i] - (c - x[n - 1 - i])
    leftmaxdouble.append(currentmax)
ans = 0
for i in range(n):
    if n - i >= 2:
        if rightvalue[i] + leftmaxdouble[n - i - 2] > ans:
            ans = rightvalue[i] + leftmaxdouble[n - i - 2]
    elif rightvalue[i] > ans:
        ans = rightvalue[i]
for i in range(n):
    if n - i >= 2:
        if leftvalue[i] + rightmaxdouble[n - i - 2] > ans:
            ans = leftvalue[i] + rightmaxdouble[n - i - 2]
    elif leftvalue[i] > ans:
        ans = leftvalue[i]
print(ans)
