(n, k) = map(int, input().split())
s = input()
flag = True
for i in range(n):
    if s.count(s[i]) > k:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
