s = list(input())
flag = 0
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        flag = 1

print('Bad' if flag == 1 else 'Good')
