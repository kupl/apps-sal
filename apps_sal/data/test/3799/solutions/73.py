s = input()
if s[0] == s[-1]:
    print(('First', 'Second')[len(s) % 2])
else:
    print(('Second', 'First')[len(s) % 2])
