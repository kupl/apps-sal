s = str(input())
isBad = False
for i in range(3):
    if s[i] == s[i + 1]:
        isBad = True
if isBad:
    print('Bad')
else:
    print('Good')
