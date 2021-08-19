"""
priority-queue
"""
import copy
num_list = list(map(int, input('').split(' ')))
rank = num_list[3]
lists = []
queue = []
for i in range(3):
    a_list = list(map(int, input('').split(' ')))
    list.sort(a_list, reverse=True)
    if num_list[i] <= rank:
        lists.append(a_list)
    else:
        lists.append(a_list[:rank])
queue.append([lists[0][0] + lists[1][0] + lists[2][0], 0, 0, 0])
for i in range(rank):
    poped = queue.pop(0)
    print(poped[0])
    if i == rank - 1:
        break
    for j in range(3):
        if len(lists[j]) > poped[j + 1] + 1:
            to_append = copy.copy(poped)
            to_append[j + 1] += 1
            to_append[0] += lists[j][to_append[j + 1]] - lists[j][poped[j + 1]]
            if len(queue) == 0:
                queue.append(to_append)
                continue
            Done = True
            for k in range(len(queue)):
                if queue[k] == to_append:
                    Done = False
                    break
                elif queue[k][0] < to_append[0]:
                    queue = queue[:k] + [to_append] + queue[k:]
                    Done = False
                    break
            if Done == True:
                queue.append(to_append)
    if len(queue) > rank - i - 1:
        queue = queue[:rank - i - 1]
