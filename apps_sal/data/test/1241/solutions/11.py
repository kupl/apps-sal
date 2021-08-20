(n, k) = map(int, input().split())
s = list(map(int, input().split()))
ans = 0


def get(x):
    return 1 - x


l = 0
r = -1
cnt = 0
L = n
R = 0
while l < n:
    while r + 1 < n and cnt + get(s[r + 1]) <= k:
        cnt += get(s[r + 1])
        r += 1
    now = r - l + 1
    if now > ans:
        ans = now
        L = l
        R = r
    cnt -= get(s[l])
    l += 1
for i in range(L, R + 1):
    s[i] = 1
print(ans)
print(' '.join(map(str, s)))
