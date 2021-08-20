(n, k, c) = list(map(int, input().split()))
s = input()
INF = float('inf')
left = [0] * (n + 1)
right = [0] * (n + 1)
mleft = 0
last = -c - 1
for i in range(n):
    if s[i] == 'o' and i - last > c:
        mleft += 1
        last = i
        left[i + 1] = mleft
mright = 0
last = -c - 1
t = s[::-1]
for i in range(n):
    if t[i] == 'o' and i - last > c:
        mright += 1
        last = i
        right[i + 1] = mright
for i in range(n):
    left[i + 1] = max(left[i + 1], left[i])
    right[i + 1] = max(right[i + 1], right[i])
left.remove(left[0])
right.remove(right[0])
right = right[::-1]
left.append(0)
right.append(0)
ans = []
for i in range(1, n + 1):
    if s[i - 1] == 'o':
        if left[i - 2] + right[i] < k:
            ans.append(i)
for i in range(len(ans)):
    print(ans[i])
