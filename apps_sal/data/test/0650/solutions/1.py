NEAT = 'AEFHIKLMNTVWXYZ'
a = input()
print('YES' if all(x in NEAT for x in a) or all(x not in NEAT for x in a) else 'NO')
