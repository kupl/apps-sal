import numpy as np
import sys
input = sys.stdin.readline
N = int(input())
A = np.array(input().split(), dtype=np.int64)


def select_operation(select, N):
    result = []
    x = select.min()
    result = [0] * x
    select -= x
    N -= x
    y = select.max()
    result += list(range(N - 1, y, -1))
    N = y + 1
    result += np.setdiff1d(np.arange(N)[::2], select)[::-1].tolist()
    result += [1] * (len(select) - 1)
    result = [1 + x for x in result]
    return result


ev_sum = np.maximum(0, A[::2]).sum()
od_sum = np.maximum(0, A[1::2]).sum()
if ev_sum >= od_sum > 0:
    select = np.where(A[::2] >= 0)[0] * 2
elif od_sum > 0:
    select = np.where(A[1::2] >= 0)[0] * 2 + 1
else:
    n = np.argmax(A)
    select = np.array([n])
S = A[select].sum()
ope = select_operation(select, N)
print(S)
print(len(ope))
print('\n'.join(map(str, ope)))
select
