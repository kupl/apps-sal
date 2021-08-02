n, m, k = list(map(int, input().split()))
for i in range(n):
    li = list(map(int, input().split()))
ans = []
for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        ans.append([i, j])
if k == 0:
    print(len(ans))
    for i in ans:
        print(*i)
else:
    print(len(ans))
    for i in ans[::-1]:
        print(*i[::-1])
