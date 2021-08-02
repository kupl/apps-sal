x, y, z, k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)
c = sorted(list(map(int, input().split())), reverse=True)
ans = []
for i in range(x):
    for j in range(y):
        for l in range(z):
            if (i + 1) * (j + 1) * (l + 1) <= k:
                ans.append(a[i] + b[j] + c[l])
            else:
                break
ans.sort(reverse=True)
for i in range(k):
    print((ans[i]))
