n = int(input())
ans = 0
for c in range(n, 1, -1):
    cs = [int(x) for x in '{:02b}'.format(c)]
    if 0 not in cs or 1 not in cs[1:]:
        continue
    N = len(cs)
    for i in range(1, N - 1):
        if cs[i] == 0:
            continue
        for j in range(i + 1, N):
            if cs[j] == 1:
                continue
            left = 2 ** sum(cs[i + 1:j])
            right = 2 ** (N - j - 1)
            ans += left * right
print(ans)
