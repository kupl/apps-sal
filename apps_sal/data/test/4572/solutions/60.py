S = str(input())
no_ans = 'None'
ans_list = []
arufabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(arufabet)):
    if arufabet[i] not in S:
        ans_list.append(arufabet[i])
if len(ans_list) == 0:
    print(no_ans)
else:
    print(ans_list[0])
