s = input()
flag = False
for i in range(3):
    if s[i] == s[i + 1]:
        flag = True
if flag:
    print('Bad')
else:
    print('Good')
