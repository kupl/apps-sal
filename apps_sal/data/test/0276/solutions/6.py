# cook your dish here
# from math import * 
d = {"Power":"purple","Time":"green","Space":"blue","Soul":"orange","Reality":"red","Mind":"yellow"}; 
n = int(input())
l =[]
for _ in range(n):
    l.append(input())
print(6-n)
for ele in d:
    if d[ele] not in l:
        print(ele)
