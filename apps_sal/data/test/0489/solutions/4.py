def c(n, k):
    r = 1
    for i in range(k):
        r *= n
        n -= 1
    for i in range(2, k + 1):
        r //= i
    return r


n = int(input())
l = sorted(map(int, input().split()))
prev = l[0]
beg = 0
cnt = 0
ans = 1
for i in range(n):
    if l[i] == prev:
        cnt += 1
    else:
        ans *= c(i - beg, min(3, i) - beg)
        cnt = 1
        prev = l[i]
        beg = i
        if i > 2:
            break
if beg < 3:
    ans *= c(n - beg, 3 - beg)

print(ans)
