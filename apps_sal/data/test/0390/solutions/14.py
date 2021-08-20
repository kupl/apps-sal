import sys
f = sys.stdin
out = sys.stdout
(n, a, b) = map(int, f.readline().rstrip('\r\n').split())
c = list(map(int, f.readline().rstrip('\r\n').split()))
j = n - 1
(cost, flag) = (0, 0)
for i in range(n // 2):
    if c[i] == c[j] and c[i] == 2:
        cost += 2 * min(a, b)
    elif c[i] != c[j] and c[i] == 2:
        if c[j] == 0:
            cost += a
        else:
            cost += b
    elif c[i] != c[j] and c[j] == 2:
        if c[i] == 0:
            cost += a
        else:
            cost += b
    elif c[i] != c[j]:
        flag = 1
        break
    j -= 1
if n & 1 == 1:
    if c[n // 2] == 2:
        cost += min(a, b)
if flag == 1:
    out.write(str(-1) + '\n')
else:
    out.write(str(cost) + '\n')
