from sys import stdin as Si
from itertools import combinations_with_replacement as Cr


def __starting_point():
    n, c = list(map(int, Si.readline().split()))

    S = tuple(map(int, Si.readline().split()))  # score
    T = tuple(map(int, Si.readline().split()))  # time
    L, R = 0, 0
    for i in range(n):
        # print(S[i],sum(T[:i+1])*c,S[n-1-i],sum(T[n-1-i:])*c)
        L += max(0, S[i] - sum(T[:i + 1]) * c)
        R += max(0, S[n - 1 - i] - sum(T[n - 1 - i:]) * c)
    if L > R: print('Limak')
    elif R > L: print('Radewoosh')
    else: print('Tie')


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
