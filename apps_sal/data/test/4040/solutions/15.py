(n, m, d) = list(map(int, input().split()))
c = list(map(int, input().split()))
r = sum(c)
cur = 0
ci = 0
mmap = [0] * n
while cur < n + 1 and ci < len(c):
    pi = min(cur + d, n - r + 1)
    for j in range(pi, pi + c[ci]):
        mmap[j - 1] = ci + 1
    cur = pi + c[ci] - 1
    r -= c[ci]
    ci += 1
if cur + d >= n + 1:
    print('YES')
    print(' '.join(map(str, mmap)))
else:
    print('NO')
