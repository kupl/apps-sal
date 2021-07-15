n = int(input())
list_d = sorted([int(input()) for i in range(0, n)], reverse=True)
list_ans = []
for i in range(0, len(list_d)):
    if list_d[i] not in list_ans:
        list_ans.append(list_d[i])
print(len(list_ans))
