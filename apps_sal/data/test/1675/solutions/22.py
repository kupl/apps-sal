n,i,o = int(input()),[0 for z in range(10**5+1)],[]
for k in range(n):
    inp1,inp2 = list(map(int,input().split()))
    i[inp1]+=1; o.append(inp2)
for k in o: print(n-1+i[k], n-1-i[k])
