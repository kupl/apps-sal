s = input()
sol = ''
sol += '1' * s.count('1')
sol += '2' * s.count('2')
sol += '3' * s.count('3')
print('+'.join(sol))
