n = int(input())
p = list(map(int, input().split()))
i = 0
ans = []
target = 1
while i < n:
    if p[i] == target:
        for j in range(i, target - 1, -1):
            (p[j], p[j - 1]) = (p[j - 1], p[j])
            ans.append(j)
        target = i + 1
    i += 1
if len(ans) != n - 1:
    print(-1)
elif p != [i for i in range(1, n + 1)]:
    print(-1)
else:
    for j in ans:
        print(j)
