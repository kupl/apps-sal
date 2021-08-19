S = input()
code_list = []
for code in S:
    code_list.append(code)
answer = code_list[0] != code_list[1] != code_list[2] != code_list[3]
if answer:
    print('Good')
else:
    print('Bad')
