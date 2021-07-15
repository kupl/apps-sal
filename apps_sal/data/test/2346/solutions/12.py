n = int(input())
mass = [0 for i in range(n + 10)]
arr = [0 for i in range(n + 10)]
nnn = [0 for i in range(n + 10)]
for i in range(n):
    a, b = map(int, input().split())
    if a != -1:
        mass[a] += 1
        arr[a] += b
    nnn[i + 1] = b
ans = []
for i in range(n):
    if mass[i + 1] == arr[i + 1] and nnn[i + 1] == 1:
        ans.append(i + 1)
if len(ans) == 0:
    ans.append(-1)
for i in ans:
    print(i, end = ' ')
