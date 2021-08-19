# Name : Sachdev Hitesh
# College : GLSICA

user = input()
resu = user[::-1]
s = len(user)
# print(s)
c = 0
if user == resu:
    for i in user:
        if i == 'A' or i == 'H' or i == 'I' or i == 'O' or i == 'T' or i == 'V' or \
                i == 'W' or i == 'X' or i == 'Y' or i == 'M' or i == 'U':
            c = c + 1
if c == s:
    print("YES")
else:
    print("NO")
