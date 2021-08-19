n = int(input())
s = input()
torem = n - 11
if s[:torem + 1].count('8') > (torem + 1) // 2:
    print('YES')
else:
    print('NO')
