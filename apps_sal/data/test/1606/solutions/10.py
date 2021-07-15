# from operator import and_, xor
# from functools import reduce
# from itertools import chain
from sys import stdin
input = stdin.readline

n = int(input())
l = list(list(map(int, input().split())) for _ in range(n))
q = int(input())
output = []
ans = 0

# We don't care about anything except for the trace of the matrix
# Why? write the matrix with symbols not 0's and 1's

for i in range(n):
    ans ^= l[i][i]

for i in range(q):
    command = input()
    if command[0] == '3':
        output.append(ans)
    else:
        ans^=1
# Why? first, put in mind that all we care about is the trace of the matrix
# We will flip either the column or the row, we will be facing two possibilities
# either to subtract from the original answer or do addition ... well thanks to GF(2)
# both of the operations are just XORing 

print(''.join([*map(str, output)]))
