import numpy as np


def getDivisor(n):
    divisor = []
    tmp = n
    for i in range(2, int(n**0.5) + 1):
        cnt = 1
        d = [1, ]
        while tmp % i == 0:
            d.append(i**cnt)
            tmp //= i
            cnt += 1
        if cnt > 1:
            divisor.append(d)
    if tmp != 1:
        divisor.append([1, tmp])
    if divisor == []:
        divisor.append([1, n])

    divisor_mat = np.matrix(1)
    for d in divisor:
        d = np.matrix(d)
        mat = []
        for dcol in divisor_mat:
            mat.append(dcol.T * d)
        divisor_mat = np.concatenate(mat)
    divisor_mat = np.array(divisor_mat.flatten())
    divisor_mat = np.array(divisor_mat[0].tolist())
    divisor_mat.sort()
    return divisor_mat


n, k = map(int, input().split())
a = list(map(int, input().split()))

a = np.array(a)
sum_a = a.sum()
divisor = getDivisor(sum_a)
for d in divisor[::-1]:
    tmp = a % d
    idx = tmp.sum() // d
    tmp.sort()
    num_op = tmp[:-idx].sum()
    if num_op <= k:
        break
print(d)
