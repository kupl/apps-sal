s = input()
print(['Second', 'First'][(len(s) + (s[0] == s[-1])) % 2])
