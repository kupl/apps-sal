import re

N = int(input())
s = input()[:N]
s_check = s
s_check = re.sub('\(\)', '', s_check)

while len(s_check) > 0:
    for i in range(len(s_check)):
        if s_check[i] == ')':
            s = '(' + s
            s_check = '(' + s_check
            break
        elif s_check[i] == '(':
            break

    for i in range(len(s_check)):
        if s_check[-i-1] == '(':
            s = s + ')'
            s_check = s_check + ')'
            break
        elif s_check[-i-1] == ')':
            break

    s_check = re.sub('\(\)', '', s_check)

print(s)
