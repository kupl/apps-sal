a, b, k = map(int, input().split())

ans = {}
for i in range(a, a + k):
    if i <= b:
        ans.setdefault(i, 0)
        ans[i] += 1
    else:
        break
for i in range(b - (k - 1), b + 1):
    if a <= i:
        ans.setdefault(i, 0)
        ans[i] += 1
    else:
        break
for i in ans.keys():
    print(i)
