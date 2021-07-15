n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
c = [-1]*256

ans = [0]*n
for i in range(n):
    if c[a[i]] == -1:
        for j in range(a[i], max(-1, a[i]-k), -1):
            if c[j] != -1:
                if (c[j] +k) > a[i]:
                    c[a[i]] = c[j]
                else:
                    c[a[i]] = j+1
                break
        if c[a[i]] == -1:
            c[a[i]] = max(0, a[i]-k+1)
        for xx in range(c[a[i]], a[i]):
            c[xx] = c[a[i]]
    ans[i] = str(c[a[i]])

print(' '.join(ans))

