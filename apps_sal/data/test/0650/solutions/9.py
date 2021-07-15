lin = set(list('WETYIAFHKLZXVNM'))
s = input()
print('YES' if len(set(list(s)).intersection(lin)) in [len(set(list(s))), 0] else 'NO')

