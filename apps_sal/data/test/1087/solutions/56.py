(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
x = 0
for i in range(k.bit_length() - 1, -1, -1):
    cnt = 0
    for j in range(n):
        if a[j] >> i & 1 == 1:
            cnt += 1
    if cnt < (n + 1) // 2:
        t = x + (1 << i)
        if t <= k:
            x = t
ans = 0
for ai in a:
    ans += ai ^ x
print(ans)
