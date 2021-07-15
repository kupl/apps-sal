import math

N = int(input())
A = []
B = []
num_list = []

root = math.floor(math.sqrt(N))


def solv(N):
    for i in range(1,root+1):
        if N%i == 0:
            A.append(i)
            B.append(N//i)
    for a,b in zip(A,B):
        a_str = str(a)
        b_str = str(b)
        a_num = len(a_str)
        b_num = len(b_str)
        if a_num > b_num:
            num_list.append(a_num)
        elif a_num < b_num:
            num_list.append(b_num)
        else:
            num_list.append(a_num)
    return print(min(num_list))

solv(N)

