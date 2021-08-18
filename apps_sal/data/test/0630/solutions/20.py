n, k = map(int, input().split())
k = min(k, n - 1)
a = list(map(lambda x: int(x) - 1, input().split()))
kek = [0 for i in range(n)]
ans = [0 for i in range(n)]
for i in range(n):
    if a[i] == -1:
        cur_l = max(0, i - k)
        cur_r = min(i + k, n - 1)
        ans[i] = (i - cur_l) + (cur_r - i) + 1
    else:
        x = ans[a[i]]
        d = (i - a[i] - 1)
        if d >= 2 * k:
            x += min(k, i) + min(k, n - i - 1) + 1
        else:
            o = 0
            cur_l = max(0, i - k)
            cur_r = min(i + k, n - 1)
            his_l = min(0, a[i] - k)
            his_r = min(a[i] + k, n - 1)
            if 2 * k >= d >= k:
                o = d - 2 * (k)
            elif d == k - 1:
                o = (-d - 2)
            else:
                o = (-(his_r - a[i] + 1)) - (a[i] - cur_l)
            x += (i - cur_l) + (cur_r - i) + 1 + o
        ans[i] = x
print(' '.join(map(str, ans)))
