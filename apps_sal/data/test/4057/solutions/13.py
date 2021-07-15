n = int(input())
s = [int(i) for i in input().split()]

maxT = 0
for i in s:
    t=0
    for j in s:
        if(i == j):
            t+=1
    if(t>maxT):
        maxT = t
print(maxT)
