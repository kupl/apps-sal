n = int(input())
c = [0] * 26
a = []
for i in range(n):
    a.append(input().strip())
    for k in a[-1]:
        c[ord(k) - ord('a')] += 1
b = True
for i in range(n):
    if a[i][i] != a[0][0] or a[0][0] != a[i][n - i - 1]:
        b = False
        break
if b == False:
    print('NO')
elif a[0][0] == a[0][1]:
    print('NO')
elif c[ord(a[0][1]) - ord('a')] != n * n - 2 * n + 1:
    print('NO')
else:
    print('YES')
