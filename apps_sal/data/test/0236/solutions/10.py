s = input()
c1 = s.count('-')
c2 = s.count('o')
if c2 == 0 or (c2 != 0 and c1 % c2 == 0):
    print("YES")
else:
    print("NO")
