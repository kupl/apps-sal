lis = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
s = input()
ans = True
for i in lis:
    if i in s:
        ans = False
if ans:
    print('Good')
else:
    print('Bad')
