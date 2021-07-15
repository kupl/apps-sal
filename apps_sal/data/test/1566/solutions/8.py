n = int(input())
aux = []
grid = []
flag = True
ans = -1
um = 0
dois = 0
quatro = 0
while(n):
        n-=1
        x = str(int(input()))
        if(x!='0'):
                aux.append(x)
for i in aux:
        txt = ''
        for j in i:
                if(j!='0'):
                        txt+=j
        grid.append(txt)
for i in grid:
        for j in i:
                if(j == '1'):
                        um+=1
                if(j == '2'):
                        dois+=1
                if(j == '4'):
                        quatro+=1
        if(ans==-1 or len(i)==ans):
                ans = len(i)
        else:
                flag = False
if(um!=4 or dois!=len(grid)*2+len(grid[0])*2-8 or quatro!=(len(grid)*len(grid[0]))-(len(grid)*2+len(grid[0])*2-4)):
        flag = False
if(flag):
        for i in range(0, len(grid)):
                if(len(grid)-i-1 < i):
                        break
                if(grid[i] != grid[len(grid)-i-1]):
                        flag = False
        for i in range(0, len(grid)):
                for j in range(0, len(grid[0])):
                        if(len(grid)-j-1 < j):
                                break
                        if(grid[i][j] != grid[i][len(grid[i])-j-1]):
                                flag = False
if(flag and ans!=-1):
        print('Yes')
else:
        print('No')
