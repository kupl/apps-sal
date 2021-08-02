N = int(input())
l_list = [2, 1]
for i in range(2, N + 1):
    a = l_list[i - 1] + l_list[i - 2]
    l_list.append(a)
print(l_list[N])
