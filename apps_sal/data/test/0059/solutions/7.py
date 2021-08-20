n = int(input())
a = list(map(int, input().split()))
s = list(input())
s.append(1)
(rec, q) = ([], 0)
for i in range(n):
    rec.append(q + a[i])
    q = rec[i]
flag = True
for i in range(n):
    if s[i] == '0' and rec[i] > (i + 1) * (i + 2) // 2:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
