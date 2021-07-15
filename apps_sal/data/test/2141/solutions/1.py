n=int(input())
for i in range(n):
    s=""
    for j in range(n):
        if (i+j)%2==0:s+="W"
        else:s+="B"
    print(s)
