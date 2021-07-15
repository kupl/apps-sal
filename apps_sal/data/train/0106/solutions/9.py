t = int(input())
final = []
for k in range(t):
    n = int(input())
    skl = []
    for i in range(n):
        a, b = map(int, input().split())
        skl.append((a, -1, i))
        skl.append((b, 1, i))
    skl.sort()
    m = 0
    ans = ['0']*n
    for i, p in enumerate(skl):
        if m == 0 and i != 0:
            for j in range(i, 2*n):
                ans[skl[j][2]] = '2'
            break

        m -= p[1]
        if p[1] == -1:
            ans[skl[i][2]] = '1'
    if not '2' in ans:
        final.append('-1')
    else:
        final.append(' '.join(ans))
print('\n'.join(final))
