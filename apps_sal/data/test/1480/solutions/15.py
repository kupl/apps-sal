n, k = map(int, input().split())
a = list(map(int, input().split()))
used = [0] * n
ans = ""
cnt = 1
tmp = n
for i in range(k):
    cur = a[i] % n
    while cur > 0:
        if used[cnt] == 0:
            cur -= 1
        cnt += 1
        cnt = cnt % tmp
    if cnt != 0:
        ans += str(cnt) + " "
    else:
        ans += str(tmp) + " "
    used[cnt - 1] = 1
    while used[cnt] == 1:
        cnt += 1
        cnt %= tmp
    cnt += 1
    cnt %= tmp
    n -= 1
print(ans)
