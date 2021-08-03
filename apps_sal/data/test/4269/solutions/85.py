s = input()
tmp1 = s[0]
for i in range(1, len(s)):
    tmp2 = s[i]
    if tmp1 == tmp2:
        print('Bad')
        return
    else:
        tmp1 = tmp2
print('Good')
