n, m = [int(i) for i in input().split()]
a = input().split()
b = [0] * n
ans = []
for i in range(1, n):
    if a[i] != a[i - 1]:
        b[i] = i
    else:
        b[i] = b[i - 1]
for i in range(m):
    c = input().split()
    c[1] = int(c[1])
    c[0] = int(c[0])
    if a[c[1] - 1] != c[2]:
        ans.append(str(c[1]))
    elif b[c[1] - 1] <= c[0] - 1:
        ans.append(str(-1))
    else:
        ans.append(str(b[c[1] - 1]))
print('\n'.join(ans))
