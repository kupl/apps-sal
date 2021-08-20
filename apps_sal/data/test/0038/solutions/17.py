(n, l) = list(map(int, input().split()))
k = list(map(int, input().split()))
s = list(map(int, input().split()))
ki = [k[0]]
si = [s[0]]
tmp = 0
for i in range(1, n):
    ki.append(k[i] - k[i - 1])
    si.append(s[i] - s[i - 1])
ki[0] += l - k[-1]
si[0] += l - s[-1]
if ''.join(map(str, ki * 2)).find(''.join(map(str, si))) != -1:
    print('YES')
else:
    print('NO')
