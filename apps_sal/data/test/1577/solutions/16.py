input()
s = input()
if s.count('D') == s.count('A'):
    print('Friendship')  # is magic
else:
    print(['Anton', 'Danik'][s.count('D') > s.count('A')])

