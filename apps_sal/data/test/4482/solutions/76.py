import math
 
N = int(input())
A = [int(a) for a in input().split(" ")]
ave = sum(A) / N
can1 = math.floor(ave)
can2 = math.ceil(ave)
 
cost1 = sum([(a - can1) ** 2 for a in A])
cost2 = sum([(a - can2) ** 2 for a in A])
print(min([cost1, cost2]))
