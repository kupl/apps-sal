s = input()
print('YES' if s[0] == '1' and all((q == '' or q == '4' or q == '44' for q in s.split('1'))) else 'NO')
