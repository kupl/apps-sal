"""
Created on Thu Jan 21 14:59:34 2016

@author: kebl4230
"""
start = [int(entry) for entry in input().split()]
end = [int(entry) for entry in input().split()]
x_dist = abs(start[0] - end[0])
y_dist = abs(start[1] - end[1])
result = x_dist + y_dist - min(x_dist, y_dist) * (1 if (x_dist > 0 and y_dist > 0) else 0)
print(result)
