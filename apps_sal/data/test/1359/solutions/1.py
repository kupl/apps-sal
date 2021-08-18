n, e = list(map(int, input().split()))
dl = {}
for itr in range(1, n + 1):
    dl[itr] = set()
for itr in range(e):
    a1, a2 = list(map(int, input().split()))
    dl[a1].add(a2)
ans = 0
for i in range(1, n + 1):
    arr = [0] * (n + 1)
    for j in dl[i]:
        for k in dl[j]:
            if i != k:
                arr[k] += 1
    for itr in arr:
        ans += itr * (itr - 1) // 2
print(ans)
