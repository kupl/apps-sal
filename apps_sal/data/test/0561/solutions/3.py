n = int(input())
t = list(map(int, input().split()))
if n == 1:
    q = '-1'
else:
    t.sort()
    d = min(t[1] - t[0], t[-1] - t[-2])
    q = '2\n' + str(t[0] - d) + ' ' + str(t[-1] + d) if d else '1\n' + str(t[0])
    if n == 2:
        if d and d % 2 == 0:
            q = '3\n' + str(t[0] - d) + ' ' + str(t[0] + d // 2) + ' ' + str(t[-1] + d)
    else:
        for i in range(1, n):
            if t[i] - t[i - 1] != d:
                if t[i] - t[i - 1] == 2 * d and q[0] == '2':
                    q = '1\n' + str(t[i] - d)
                else:
                    q = '0'
                    break
print(q)
