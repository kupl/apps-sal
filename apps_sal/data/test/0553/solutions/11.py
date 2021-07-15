n = int(input())
codes = [tuple(input()) for i in range(n)]
mind = 13 #Dirty hack for n=1
for i in range(n-1):
    for j in range(i+1, n):
        d = sum(x!=y for x,y in zip(codes[i], codes[j]))
        if d<mind:
            mind = d
print((mind-1)//2)
