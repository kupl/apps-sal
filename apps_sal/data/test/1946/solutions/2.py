"""
Created on Sun May 27 20:07:20 2018

@st0rmbring3r
"""

cost_dict = {}

a = int(input())
for i in range(a):
    x, y = [int(x) for x in input().split()]
    cost_dict[x] = y

b = int(input())
for i in range(b):
    x, y = [int(x) for x in input().split()]
    if x in cost_dict:
        y2 = cost_dict[x]
        cost_dict[x] = max(y, y2)
    else:
        cost_dict[x] = y

print(sum(cost_dict.values()))
