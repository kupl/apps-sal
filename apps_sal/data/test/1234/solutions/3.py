def func(n):
    return n[1]


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = [[a[i], i] for i in range(len(a))]
b.sort(reverse=True)
b = b[:m * k]
b.sort(key=func)
ans = []
ans2 = 0
for i in range(0, len(b), 1):
    if (i + 1) % m == 0:
        ans.append(b[i][1] + 1)
    ans2 += b[i][0]
print(ans2)
print(' '.join(map(str, ans[:-1])))
