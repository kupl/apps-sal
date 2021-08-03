a, b, f, k = list(map(int, input().split()))
ans = 0
c = b
if b < f:
    ans = -1
else:
    c -= f
for i in range(k):
    if ans == -1:
        break
    if i % 2 == 0:
        d = a - f
    else:
        d = f
    if i < k - 1:
        d *= 2
    if b < d:
        ans = -1
    elif c < d:
        ans += 1
        c = b
    c -= d

print(ans)
