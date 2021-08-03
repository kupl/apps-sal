n = int(input())
s = input()
cnt = 0
for i in range(n - 10):
    if s[i] == '8':
        cnt += 1
if cnt >= ((n - 9) // 2):
    print('YES')
else:
    print('NO')
