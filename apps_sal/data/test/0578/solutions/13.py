S = input()

A, B = S.split('e')

a1, a2 = A.split('.')
s1, s2 = a1[:] + a2[:int(B)], a2[int(B):]

while len(s1 + s2) < int(B) + 1:
    s1 = s1 + '0'

if len(s2) == 0 or int(s2) == 0:
    print(s1)
else:
    print(s1 + '.' + s2)
