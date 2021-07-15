n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort(reverse = True)
cur_len, res = 1, []
while k > 0 and cur_len <= n:
    for i in range(cur_len, n+1):
        print(cur_len, *res, a[i-1])
        k -= 1
        if k == 0: break
    res.append(a[cur_len-1])
    cur_len += 1

