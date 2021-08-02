temp = input().split(' ')
num_list = [int(s) for s in temp]
ans_list = []

for i in range(2):
    for j in range(2, 4, 1):
        ans = num_list[i] * num_list[j]
        ans_list.append(ans)

print(max(ans_list))
