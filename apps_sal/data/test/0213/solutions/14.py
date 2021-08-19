(m, n) = map(int, input().split())
arr = []
for i in range(n):
    (a, b) = map(int, input().split())
    arr.append((a, b))
ans = set()
for k in range(1, 150):
    fl = True
    for i in range(n):
        if (arr[i][0] - 1) // k + 1 != arr[i][1]:
            fl = False
            break
    if fl:
        ans.add((m - 1) // k + 1)
if len(ans) == 1:
    for i in ans:
        print(i)
else:
    print(-1)
