n = int(input())
s = input()
if s[:n - 10].count('8') > (n - 11) // 2:
    print('YES')
else:
    print('NO')
