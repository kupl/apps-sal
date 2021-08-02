k = int(input())
s = ''
n = list()
for i in range(4):
    a = input()
    s = s + a
for i in range(1, 10):
    n.append(s.count(str(i)))
if max(n) > 2 * k:
    print('NO')
else:
    print('YES')
