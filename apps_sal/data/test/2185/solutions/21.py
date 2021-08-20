"""
Name : Jaymeet Mehta
id :mj_13
Problem : Single push
"""
from sys import stdin, stdout
test = int(stdin.readline())
for _ in range(test):
    N = int(stdin.readline())
    A = [int(x) for x in stdin.readline().split()]
    B = [int(x) for x in stdin.readline().split()]
    indices = []
    values = []
    flag = True
    for i in range(N):
        if A[i] != B[i]:
            if B[i] < A[i]:
                flag = False
                break
            values.append(B[i] - A[i])
            indices.append(i)
    if not flag:
        print('NO')
        continue
    if len(set(values)) > 1:
        flag = False
    for i in range(1, len(indices)):
        if indices[i] - indices[i - 1] != 1:
            flag = False
            break
    print('YES') if flag else print('NO')
