n = int(input())
a = list(map(int, input().split()))

cnt, su, r = 0, 0, 0
for l in range(n):
    while r < n and su + a[r] == su ^ a[r]:
        su += a[r]
        r += 1
    cnt += r - l
    if l == r:
        r += 1
    else:
        su -= a[l]
print(cnt)
