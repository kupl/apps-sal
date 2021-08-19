(n, m) = list(map(int, input().split()))
l = input().split()
(L, ans) = ([0 for i in range(n)], [])
L[0] = -1
for i in range(1, n):
    if l[i] == l[i - 1]:
        L[i] = L[i - 1]
    else:
        L[i] = i
for i in range(m):
    s = input().split()
    b = int(s[1])
    if l[b - 1] != s[2]:
        ans += [str(b)]
    elif L[b - 1] >= int(s[0]):
        ans += [str(L[b - 1])]
    else:
        ans += ['-1']
print('\n'.join(ans))
