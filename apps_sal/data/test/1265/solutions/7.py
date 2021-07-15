s1 = input()
s2 = input()
if ('1' in s1 and '1' not in s2) or ('1' in s2 and '1' not in s1) or len(s1) != len(s2):
    print('NO')
else:
    print('YES')
