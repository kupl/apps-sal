(x, y, z, K) = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))[::-1]
b = sorted(list(map(int, input().split())))[::-1]
c = sorted(list(map(int, input().split())))[::-1]
ans = []
for i in range(x):
    for j in range(y):
        if i * j > K:
            break
        for k in range(z):
            if i * j * k > K:
                break
            ans.append(a[i] + b[j] + c[k])
ans = sorted(ans)[::-1]
for i in range(K):
    print(ans[i])
