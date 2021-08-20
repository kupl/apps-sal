(n, m) = map(int, input().split())
(k, s) = ([], [])
for i in range(m):
    inp = list(map(int, input().split()))
    (k_, s_) = (inp[0], inp[1:])
    k.append(k_)
    s.append(s_)
p = list(map(int, input().split()))
ans = 0
for bit in range(1 << n):
    flg = True
    for i in range(m):
        cnt = 0
        for e in s[i]:
            e -= 1
            if bit & 1 << e:
                cnt += 1
        if cnt % 2 != p[i]:
            flg = False
    if flg:
        ans += 1
print(ans)
