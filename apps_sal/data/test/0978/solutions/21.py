k = int(input())
s = ''.join((input().replace('.', '') for i in range(4)))
print('NO' if len(s) > 0 and max((s.count(c) for c in set(s))) > 2 * k else 'YES')
