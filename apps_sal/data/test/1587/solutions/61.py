n = int(input())
mozi = input()
a_list = []
for i in range(n):
    if mozi[i] == 'W':
        a_list.append(0)
    else:
        a_list.append(1)
r_count = sum(a_list)
print(r_count - sum(a_list[0:r_count]))
