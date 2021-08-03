s = '\n'.join([input() for _ in range(int(input()))])
ns = s.replace('OO', '++', 1)
print('YES\n' + ns if ns != s else 'NO')
