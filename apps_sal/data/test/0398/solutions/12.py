# Author: Maharshi Gor

def read(type=int):
    return type(input())

def read_arr(type=int):
    return [type(token) for token in input().split()]

n = read()
A =  read_arr()

A.sort()
found = False
for i in range(len(A)-2):
    if A[i] + A[i+1] > A[i+2]:
        found = True
        break
if found:
    print("YES")
else:
    print("NO")
