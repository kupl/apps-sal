(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
v = set()
ans = []
for i in range(len(a)):
    if a[i] not in v:
        v.add(a[i])
        ans.append(i + 1)
    if len(ans) == k:
        break
if len(ans) == k:
    print('YES')
    print(' '.join(map(str, ans)))
else:
    print('NO')
