import copy
N = int(input())
A_list = []
for _ in range(N):
    A_list.append(int(input()))
sort_list = copy.deepcopy(A_list)
sort_list.sort()
a_max = sort_list[-1]
a_max_second = sort_list[-2]
if a_max == a_max_second:
    for _ in range(N):
        print(a_max)
else:
    for i in range(N):
        if A_list[i] == a_max:
            print(a_max_second)
        else:
            print(a_max)
