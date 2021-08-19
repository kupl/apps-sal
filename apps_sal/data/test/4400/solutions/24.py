s = input()
(l, r) = [False, False]
if s[0] == s[1] and s[0] == 'R':
    l = True
if s[1] == s[2] and s[1] == 'R':
    r = True
if l and r:
    print(3)
elif l or r:
    print(2)
elif s[0] == 'R' or s[1] == 'R' or s[2] == 'R':
    print(1)
else:
    print(0)
