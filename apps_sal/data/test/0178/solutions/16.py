n = int(input())
s = input()
t = s[:-10]
cnt = t.count('8')
if len(t) - cnt > cnt:
    print('NO')
else:
    print('YES')
