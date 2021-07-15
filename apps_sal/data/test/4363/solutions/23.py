k, s = map(int,input().split())

count=0
for X in range(k+1):
    for Y in range(k+1):
        Z = s - X - Y
        if k>=Z>=0:
            count+=1

print(count)
