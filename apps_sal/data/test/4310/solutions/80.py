import itertools
a_lst = list(map(int, input().split()))
choice_lst = list(itertools.permutations(a_lst, 3))
cost_lst = []
for i in range(len(choice_lst)):
    cost = 0
    for j in range(3):
        tmp_cost = choice_lst[i][j]
        if j == 0:
            continue
        else:
            cost += abs(choice_lst[i][j] - choice_lst[i][j - 1])
    cost_lst.append(cost)
minimum = min(cost_lst)
print(minimum)
