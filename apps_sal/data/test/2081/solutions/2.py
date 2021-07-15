n = int(input())
a = list(map(int, input().split()))
left = [-1 for i in range(n)]
right = [n for i in range(n)]
stack = []
for i in range(n):
    while stack and a[stack[-1]] > a[i]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    stack.append(i)
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    stack.append(i)
res = 0
for i in range(n):
    res -= a[i] * (i - left[i]) * (right[i] - i)
left = [-1 for i in range(n)]
right = [n for i in range(n)]
stack = []
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    stack.append(i)
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] <= a[i]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    stack.append(i)
for i in range(n):
    res += a[i] * (i - left[i]) * (right[i] - i)
print(res)
