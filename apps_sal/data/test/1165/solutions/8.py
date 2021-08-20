(n, m) = map(int, input().split())
a = input().split()
p = [0 for i in range(n)]
p[0] = -1
ans = []
for i in range(1, n):
    if a[i] == a[i - 1]:
        p[i] = p[i - 1]
    else:
        p[i] = i - 1
for i in range(m):
    s = input().split()
    r = int(s[1])
    if a[r - 1] != s[2]:
        ans += [str(r)]
    elif p[r - 1] >= int(s[0]) - 1:
        ans += [str(p[r - 1] + 1)]
    else:
        ans += ['-1']
print('\n'.join(ans))
