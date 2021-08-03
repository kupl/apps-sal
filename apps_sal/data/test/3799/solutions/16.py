s = input()
print(['Second', 'First'][(s[0] == s[-1]) ^ (len(s) % 2)])
