# coding:utf-8

n = int(input())
nums = list(map(int, input().split(' ')))

t = [0 for i in range(6002)]

ret = 0
for i in nums:
    t[i] += 1
ret = 0
for i in range(len(t)):
    if t[i]>0:
        ret += t[i] - 1
        t[i+1] += t[i] - 1
print(ret)

'''
Input
4
1 3 1 4
Output
1

Input
5
1 2 3 2 5
Output
2
'''
