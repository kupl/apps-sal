(n, k) = list(map(int, input().split()))
s = list(map(int, input().split()))
ans = 0


def get(x):
    return 1 - x


l = 0
cnt = 0
L = n
R = 0
for i in range(n):
    cnt += get(s[i])
    while cnt > k:
        cnt -= get(s[l])
        l += 1
    if l <= i:
        now = i - l + 1
        if now > ans:
            ans = now
            L = l
            R = i
if L <= R:
    for i in range(L, R + 1):
        s[i] = 1
print(ans)
print(' '.join(map(str, s)))
