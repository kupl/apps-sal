n = int(input())
A = list(map(int, input().split()))
res_set = set()
tmp_set = set()
NumList = [0 for i in range(n)]
for i in range(n - 1, -1, -1):
    tmp_set.add(A[i])
    NumList[i] = len(tmp_set)
ans = 0
for i in range(n - 1):
    if not A[i] in res_set:
        res_set.add(A[i])
        ans += NumList[i + 1]
print(ans)
