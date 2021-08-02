N = input()
s = list(N)
if s[0] == s[1] == s[2] == 'R':
    print((3))
elif ((s[0] == s[1] == 'R') and (s[2] == 'S')) or ((s[2] == s[1] == 'R') and (s[0] == 'S')):
    print((2))
elif s[0] == s[1] == s[2] == 'S':
    print((0))
else:
    print((1))
