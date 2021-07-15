a, b = input(), input()
if len(a) != len(b): print('NO')
else: print('NO' if ('1' in a) ^ ('1' in b) else 'YES')
