n = int(input())
s = input()
c = 0
co = 0
for i in range(1, len(s)):
    if s[i - 1] + s[i] == 'SF':
        c += 1
    elif s[i - 1] + s[i] == 'FS':
        co += 1
if c > co:
    print('YES')
else:
    print('NO')
