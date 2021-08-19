(n, k) = map(int, input().split())
r = n % (2 * k + 1)
out = []
if r >= k + 1:
    cnt = r - k
    while cnt < n:
        out.append(cnt)
        cnt += 2 * k + 1
else:
    cut1 = (r + 2 * k + 1) // 2
    cut2 = (r + 2 * k + 2) // 2
    cnt = cut1 - k
    if cnt == 0:
        cnt += k + 1
    while cnt <= n:
        out.append(cnt)
        cnt += 2 * k + 1
print(len(out))
out = map(str, out)
print(' '.join(out))
