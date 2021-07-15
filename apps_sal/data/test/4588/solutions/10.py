# import math
# import statistics
# import itertools
# a=int(input())
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
A,B= list(map(str,input().split()))
# f = list(map(int,input().split()))
# g = [input().split for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen

lis=["A","B", "C", "D", "E", "F"]
if lis.index(A)<lis.index(B):
    print("<")
elif lis.index(A)==lis.index(B):
    print("=")
else:
    print(">")


