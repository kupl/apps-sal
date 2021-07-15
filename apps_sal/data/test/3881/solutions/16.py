def __starting_point():
    n,m = list(map(int,input().split(' ')))
    d = {}
    depo,res = {},[]
    def bazinga(s):
        if s in depo:   return depo[s]
        if s[0] not in d:  depo[s]=0
        else:
            ans=0
            for aa in d[s[0]]:
                if len(aa+s[1:])==n:
                    ans+=1
                    #res.append(aa+s[1:])   #if problem is to find string
                elif len(aa+s[1:])>n:
                    continue
                else:
                    ans+=bazinga(aa+s[1:])
            depo[s]=ans
        return depo[s]

    for i in range(m):
        ai,bi = list(map(str,input().split(' ')))
        if bi in d:     d[bi] +=[ai]
        else:           d[bi]=[ai]
    print(bazinga('a'))
    #print(len(set(res)))

                    
                
                
                

'''
    A = input()
    stack = []      #Real Stack
    Graph = {
        ')':'('
        }
    count = 0
    def black(A):
        #p for possibility
        stak =[]
        for e in A:
            if e in ['(']:
                stak.append(e)
            else:
                if stak==[] or Graph[e]!=stak[-1]:
                    p=False
                else:
                    stak.pop(len(stak)-1)     #pop last 
        if len(stak) ==0:
            p=True
        else:
            p=False
        if not p:   return [0]
        else:
            #stak is not empty
            stak = []
            count = []
            for e in range(len(A)):
                if A[e]=='(' or stak==[]:  stak.append(A[e])
                else:
                    if A[e]==')' and Graph[A[e]]==stak[-1]:
                        while Graph[A[e]]==stak[-1]:
                            stak.pop(-1)
                            if e==len(A)-1: break
                            e+=1
                            if A[e]=='(' or stak==[]:   break
                        count.append(1)
            return count

    rov = []
    P = False 
    for e in A:
        if e in ['(']:  stack.append(e)
        else:
            if stack!=[]:
                stack.append(e)
                if stack.count('(')==stack.count(')'):
                    x=black(stack)
                    if x!=[0]:    P = True
                    if x==[1]:
                        rov.append(1)
                    else:
                        rov.append(sum(x[:-1]))
                    stack=[]
    if not P:   print(0)
    else:
        pro =1
        for i in rov:   pro*=i
        print(pro)
    
'''

__starting_point()
