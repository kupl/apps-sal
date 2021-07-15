from math import*
from random import*

n = int(input()) * 2
A = list(map(int, input().split()))
amount = [0] * 101

B = []
for i in range(n):
    if amount[A[i]] < 2:
        amount[A[i]] += 1
        B += [(A[i], i)]
B.sort()
x, y = [], []
for i in range(len(B)):
    if(i % 2 == 0):
        x.append(B[i][1])
    else:
        y.append(B[i][1])
lolka = 0
aaa = 0
# print(x)
# print(y)
print(len(x) * len(y))
for i in range(n):
    if i in x:
        lolka += 1
        aaa += 1
        print(1, end = ' ')
    elif i in y:
        print(2, end = ' ')
    else:
        if len(x) - lolka + aaa < n // 2:
            print(1, end = ' ')
            aaa += 1
        else:
            print(2, end = ' ')
print()

# B, C = [], []
# for i in range(n):


# S = list(set(A))
# where = [0] * 101
# am1, am2 = 0, 0
# for i in range(len(S)):
#     if(i % 2 == 0):
#         where[S[i]] = 1
#         am1 += 1
#     else:
#         where[S[i]] = 2
#         am2 += 1
# used = [0] * 201
# for i in range(n):
#     if not used[A[i]]:
#         print(where[A[i]])
#         used[A[i]] = True
#     else:
#         print(3 - where[A[i]])
