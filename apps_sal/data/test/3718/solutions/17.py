def __starting_point():
    n = int(input())
    b = sorted(set(map(int, input().split(' '))))
    for i in range(len(b) - 2):
        if len(set(b[i:i + 3])) == 3:
            if b[i + 2] - b[i] <= 2 and b[i + 2] - b[i + 1] <= 1:
                print('YES')
                break
    else:
        print('NO')


'''
    A = input()
    stack = []      
    Graph = {
        ')':'('
        }
    count = 0
    def black(A):
        stak =[]
        for e in A:
            if e in ['(']:
                stak.append(e)
            else:
                if stak==[] or Graph[e]!=stak[-1]:
                    p=False
                else:
                    stak.pop(len(stak)-1)     
        if len(stak) ==0:
            p=True
        else:
            p=False
        if not p:   return [0]
        else:
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
