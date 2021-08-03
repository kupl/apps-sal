n, k, l = list(map(int, input().split()))
a = sorted(list(map(int, input().split(' '))))
index = 0
for i in a:
    if i > a[0] + l:
        break
    index += 1
ok = index - n
if ok < 0:
    print(0)
else:
    ans = 0
    cur = 0
    for i in range(n):
        ans += a[cur]
        use = min(k - 1, ok)
        ok -= use
        cur += 1 + use
    print(ans)
