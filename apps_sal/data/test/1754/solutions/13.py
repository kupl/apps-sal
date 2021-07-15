n, m, k = map(int, input().split())
peps = list(map(int, input().split()))
schs = list(map(int, input().split()))
want = list(map(int, input().split()))
ls = [[] for i in range(m)]
for i in range(n):
    ls[schs[i] - 1].append([peps[i], i])
ans = k
for sch in ls:
    if (max(sch)[1] + 1) in want:
        ans -= 1
print(ans)
