n = int(input())
s = list(input())
cnt = 0
for i in range(0, n, 2):
    if s[i] == 'a' and s[i + 1] == 'a':
        cnt += 1
        s[i] = 'b'
    elif s[i] == 'b' and s[i + 1] == 'b':
        cnt += 1
        s[i] = 'a'
print(cnt)
print(''.join(s))

