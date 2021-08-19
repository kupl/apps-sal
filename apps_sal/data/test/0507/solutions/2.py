n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = [0 for _ in range(n)]
used = [False for _ in range(n + 1)]
idx = []
for i in range(n):
    if a[i] == b[i]:
        ans[i] = a[i]
        used[a[i]] = True
    else:
        idx.append(i)
unused = []
for i in range(1, n + 1):
    if not used[i]:
        unused.append(i)
if len(unused) == 1:
    ans[idx[0]] = unused[0]
elif a[idx[0]] != unused[0] and a[idx[1]] != unused[1] or (b[idx[0]] != unused[0] and b[idx[1]] != unused[1]):
    ans[idx[0]] = unused[1]
    ans[idx[1]] = unused[0]
else:
    ans[idx[0]] = unused[0]
    ans[idx[1]] = unused[1]
print(' '.join(map(str, ans)))
