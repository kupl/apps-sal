import numpy as np
N = int(input())
list_all =np.zeros((9,9))
num_list = [str(i) for i in range(1,N+1)]
overlap = [0 for i in range(9)]
for i in range(N):
    head = int(num_list[i][0])
    length = len(num_list[i])
    tail = int(num_list[i][length -1])
    if (head == 0) or (tail == 0):
        continue
    list_all[head-1,tail -1] += 1
sum1 = 0
for i in range(9):
    for j in range(i+1):
        if i ==j:
            sum1 += (list_all[i,j] * list_all[j,i])
        else:
            sum1 += (list_all[i,j] * list_all[j,i]) *2
print(int(sum1))
