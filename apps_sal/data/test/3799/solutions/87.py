s = input()
t = ("First", "Second")
print(t[(len(s) % 2 == 0) ^ (s[0] == s[-1])])
