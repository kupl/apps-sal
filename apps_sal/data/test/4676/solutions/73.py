O = input()
E = input()

password = ''
for o, e in zip(O, E):
    s = o + e
    password += s

if len(O) > len(E):
    print(password + O[-1])
elif len(O) < len(E):
    print(password + E[-1])
else:
    print(password)
