def dfs(i, num_str):
    nonlocal ans_list
    if i == len(str(n)):
        ans_list.append(int(num_str))
        if len(num_list) == 1:
            ans_list.append(int(num_list[0] + num_str))
        else:
            if num_list[0] == '0':
                ans_list.append(int(num_list[1] + num_str))
            else:
                ans_list.append(int(num_list[0] + num_str))
        return
    else:
        for j in num_list:
            dfs(i + 1, num_str + j)


n, k = map(int, input().split())
d = list(map(int, input().split()))

ans_list = []
num_list = []
for i in range(10):
    if i not in d:
        num_list.append(str(i))

# print(num_list)

dfs(0, '')
sort_list = sorted(ans_list)
# print(sort_list[10:])

for i in sort_list:
    if n <= i:
        print(int(i))
        break
