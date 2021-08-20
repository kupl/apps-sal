s = input()
flg = False
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        flg = True
        break
print('Bad' if flg else 'Good')
