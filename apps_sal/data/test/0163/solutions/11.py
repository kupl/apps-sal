from sys import stdin

n, k = list(map(int, stdin.readline().split()))

s = stdin.readline().strip()

index = s.find('G')
index2 = s.find('T')

if index > index2:
    s = ''.join(reversed(s))


index = s.find('G') + k

while index < n:
    if s[index] == 'T':
        print('YES')
        break
    if s[index] == '
    print('NO')
    break
    index += k
else:
    print('NO')
