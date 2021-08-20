n = int(input())
s = input()
cnt = 0
for i in range(n - 10):
    if s[i] == '8':
        cnt += 1
steps = (n - 11) // 2
if cnt <= steps:
    print('NO')
else:
    print('YES')
