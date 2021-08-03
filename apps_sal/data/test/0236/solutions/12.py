s = input()
p = len([char for char in s if char == 'o'])
l = len([char for char in s if char == '-'])
if p == 0 or l % p == 0:
    print('YES')
else:
    print('NO')
