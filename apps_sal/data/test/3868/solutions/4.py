R=lambda :list(map(int,input().split()))

n,m,k=R()

F,T=[],[]

ans=int(1e12)

for i in range(m):

    d,f,t,c=R()

    if f:F.append((d,f,c))

    else:T.append((-d,t,c))

for p in [F,T]:

    cost=[ans]*(n+1)

    s=n*ans

    q=[]

    p.sort()

    for d,t,c in p:

        #print(p)

        if c<cost[t]:

            #print(c,cost[t])

            s+=c-cost[t]

            #print(s)

            cost[t]=c

            if s<ans:

                q.append((s,d))

    p.clear()

    #print(q)

    p+=q

    #print(p)

s,t=ans,(0,0)

#print(F,T)

for f in F:

    while  f:

        if f[1]+t[1]+k<0:s=min(s,f[0]+t[0])

        elif T:

            #print(T)

            t=T.pop()

            #print(T)

           # print(t)

            continue

        #print(f)

        f=0

        #print(f)

print(s if s<ans else -1)





# Made By Mostafa_Khaled

