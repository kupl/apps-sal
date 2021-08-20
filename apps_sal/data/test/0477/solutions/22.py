(n, m, i, j, a, b) = map(int, input().split())
corners = [(1, 1), (1, m), (n, 1), (n, m)]
result = False
ans = -1
for cnt in corners:
    if abs(cnt[0] - i) % a == 0 and abs(cnt[1] - j) % b == 0:
        result = True
        (t1, t2) = (abs(cnt[0] - i) // a, abs(cnt[1] - j) // b)
        if (t1 + t2) % 2 == 0:
            if ans == -1:
                ans = max(abs(cnt[0] - i) // a, abs(cnt[1] - j) // b)
            else:
                ans = min(max(abs(cnt[0] - i) // a, abs(cnt[1] - j) // b), ans)
if ans == 0:
    print(ans)
elif not result or (i + a > n and i - a < 1) or (j + b > m and j - b < 1) or (ans == -1):
    print('Poor Inna and pony!')
else:
    print(ans)
