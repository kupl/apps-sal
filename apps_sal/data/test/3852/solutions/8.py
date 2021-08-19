n = int(input())
a = list(map(int, input().split()))
max = -9999999999999999999
min = 9999999999999999999
for i in a:
    if max < i:
        max = i
    if min > i:
        min = i
maxindex = a.index(max) + 1
minindex = a.index(min) + 1
ans = []
if min >= 0:
    for i in range(n - 1):
        ans.append([i + 1, i + 2])
elif max <= 0:
    for i in range(n - 1):
        ans.append([n - i, n - i - 1])
elif max >= abs(min):
    for i in range(1, n + 1):
        if i != maxindex:
            ans.append([maxindex, i])
    for i in range(n - 1):
        ans.append([i + 1, i + 2])
elif max < abs(min):
    for i in range(1, n + 1):
        if i != minindex:
            ans.append([minindex, i])
    for i in range(n - 1):
        ans.append([n - i, n - i - 1])
print(len(ans))
for i in ans:
    print(*i)
