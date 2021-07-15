import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    grid=[]
    for i in range(n):
        line=input()
        line=line[0:n]
        grid.append(line)
    if grid[0][1]==grid[1][0]:
        c=0
        cs=[]
        if grid[-1][-2]==grid[0][1]:
            c+=1
            cs.append([n,n-1])
        if grid[-2][-1]==grid[0][1]:
            c+=1
            cs.append([n-1,n])
        print(c)
        for x in cs:
            print(*x)
    else:
        if grid[-1][-2]==grid[-2][-1]:
            print(1)
            if grid[0][1]==grid[-1][-2]:
                print(1,2)
            else:
                print(2,1)
        else:
            print(2)
            print(2,1)
            if grid[-2][-1]==grid[0][1]:
                print(n-1,n)
            else:
                print(n,n-1)
