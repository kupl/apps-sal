s = str(input())
p = s[0] == 'R'
q = s[1] == 'R'
r = s[2] == 'R'
if p and q and r:
    print(3)
elif p and q or (q and r):
    print(2)
elif p and r or p or q or r:
    print(1)
else:
    print(0)
