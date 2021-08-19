# import math
# import statistics
# a=input()
# b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(int(i))
e1, e2, e3 = map(int, input().split())
#f = list(map(int,input().split()))
# g = [input() for _ in range(15)]
# zoro = int(a[0]*len(a))
A = e1 + e2
B = e2 + e3
C = e1 + e3
print(min(A, B, C))
