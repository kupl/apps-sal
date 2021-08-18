import numpy as np
N, M, X = map(int, input().split())
C = []
A = [[0] * M for i in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    C.append(temp[0])
    A[i] = temp[1:]
# print(A)
global_sum = 100000000
algorithm = np.array([0] * M)


def check(alg, X):
    flag = 1
    for i in range(len(alg)):
        if alg[i] < X:
            flag = 0
    if flag == 1:
        return True
    else:
        return False


flag_2 = 0


def calc(local_sum, alg, number, X):
    nonlocal global_sum
    nonlocal flag_2
    # print(local_sum,alg,number)
    if check(alg, X):
        flag_2 = 1
        if global_sum > local_sum:
            global_sum = local_sum
        return local_sum
    elif number < N:
        # 買わない
        alg = alg
        calc(local_sum, alg, number + 1, X)
        # 買う
        alg = alg + A[number]
        calc(local_sum + C[number], alg, number + 1, X)
    else:
        return


calc(0, algorithm, 0, X)
if flag_2 == 0:
    global_sum = -1
print(global_sum)
