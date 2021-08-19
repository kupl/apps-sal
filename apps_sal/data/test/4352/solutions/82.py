# import math
# import statistics
# a=input()
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#    c.append(i)
e1, e2 = map(int, input().split())
#K = input()
# f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
if e1 == e2:
    print('Draw')
elif a.index(e1) > a.index(e2):
    print('Alice')
else:
    print('Bob')
