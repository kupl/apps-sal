from collections import Counter
import math
import statistics
import itertools
# a,b=map(int,input().split())
b = int(input())
# c=[]
# for i in a:
#     c.append(int(i))
# A,B,C= map(int,input().split())
# f = list(map(int,input().split()))
#g = [list(map(lambda x: '{}'.format(x), list(input()))) for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen
# lis=[input() for i in range(a)]

lis = list(map(int, input().split()))
ans = lis[0]
word = 0

for i in range(1, b):
    word = lis[i]
    if ans <= word:
        ans = word
        word = 0
    elif ans - 1 == word:
        word = 0
    else:
        print("No")
        return

print("Yes")
