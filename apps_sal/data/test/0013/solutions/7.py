import sys
flag=True
sys.setrecursionlimit(2000000000)
c=[];st=[];
cur_adj=[]
def topo(s):#Traversing the array and storing the vertices
    nonlocal c,st,flag;
    stack = [s]
    while(stack):
        s = stack[-1]
        c[s]=1; #Being Visited
        if(cur_adj[s] < len(adjli[s])):
            cur = adjli[s][cur_adj[s]]
            if(c[cur]==0):
                stack.append(cur)
            if(c[cur]==1):
                flag=False# If Back Edge , Then Not Possible
            cur_adj[s]+=1
        else:
            c[s]=2
            st.append(str(s))
            del stack[-1]

try:
    n,k=map(int,input().split(' '))
    main=list(map(int,input().split(' ')))
    depen=[]
    for i in range(n):
    	depen.append(list(map(int,input().split(' ')))[1:]);c.append(0)
    	cur_adj.append(0)
    c.append(0)
    cur_adj.append(0)
    adjli=[]
    adjli.append(main)#Assuming Main Course at index 0 with dependencies as Main Dependency(main)
    for i in range(len(depen)):
        adjli.append(depen[i])#Appending Other Dependencies
    topo(0)#TopoLogical Sort Order
    st.pop(-1)#popping the assumed Main Couse
    if flag:# IF possible then print
        print(len(st))
        print(' '.join(st))
    else:
        print(-1)
except Exception as e:
    print(e,"error")
