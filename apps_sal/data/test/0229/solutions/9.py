from sys import stdin

n = int(stdin.readline())

numbers = set(int(x) for x in stdin.readline().split())

if len(numbers) > 3:
    print('NO')
elif len(numbers) < 3:
    print('YES')
else:
    s = sorted(numbers)
    if s[2] - s[1] == s[1] - s[0]:
        print('YES')
    else:
        print('NO')

