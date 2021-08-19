(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
r = -1
ans = 0
ans_po = 0
for l in range(n):
    if l > 0:
        if a[l - 1] == 0:
            m += 1
    while r < n - 1 and 1 - a[r + 1] <= m:
        r += 1
        if a[r] == 0:
            m = m - 1
    if r - l + 1 > ans:
        ans = r - l + 1
        ans_po = l
print(ans)
for i in range(ans_po, ans_po + ans):
    a[i] = 1
print(' '.join(map(str, a)))
