(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
last = 0
ans = []
for i in range(len(a)):
    if last != a[i] and count < k:
        ans.append(a[i] - last)
        last = a[i]
for i in range(k):
    if len(ans) <= i:
        print(0)
    else:
        print(ans[i])
