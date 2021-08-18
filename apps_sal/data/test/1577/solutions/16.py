input()
s = input()
if s.count('D') == s.count('A'):
    print('Friendship')
else:
    print(['Anton', 'Danik'][s.count('D') > s.count('A')])
