# coding: utf-8
# Your code here!

n = int(input())
A = list(map(int, input().split()))

sum_a = 0
sum_b = 0

sorted_A = sorted(A, reverse = True)

flag = 1
for i in sorted_A : 
    if flag == 1 : 
        sum_a += i
        flag = 0
    else : 
        sum_b += i
        flag = 1
        
print(sum_a - sum_b)
