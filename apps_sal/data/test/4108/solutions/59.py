"""
Created on Wed Sep 30 03:40:29 2020

@author: liang
"""
A = list()
B = list()
for i in range(26):
    A.append(list())
    B.append(list())
S = input()
T = input()


def solve():
    for i in range(len(S)):
        index = ord(S[i]) - ord('a')
        A[index].append(i)
    for a_lis in A:
        flag = False
        if a_lis:
            tmp = T[a_lis[0]]
        for t in a_lis:
            if T[t] != tmp:
                flag = True
        if flag:
            print('No')
            return
    for i in range(len(T)):
        index = ord(T[i]) - ord('a')
        B[index].append(i)
    for b_lis in B:
        flag = False
        if b_lis:
            tmp = S[b_lis[0]]
        for t in b_lis:
            if S[t] != tmp:
                flag = True
        if flag:
            print('No')
            return
    print('Yes')
    return


solve()
