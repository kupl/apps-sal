import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

import sys
sys.setrecursionlimit(10**9)
n,m,k=[int(i) for i in input().split()]
frends_num=[0 for i in range(n)]
def make_frends(m,n):
    data=[1 for i in range(m)]

    row=[]
    col=[]
    for k in range(m):
        i,j=[int(l) for l in input().split()]
        new_i=min(i,j)-1
        new_j=max(i,j)-1
        row.append(new_i)
        col.append(new_j)
        frends_num[new_i]+=1
        frends_num[new_j]+=1
    frend_sparce_matrix=csr_matrix((data, (row, col)),shape=(n,n))
    return frend_sparce_matrix


frends=make_frends(m,n)
l,labels=connected_components(frends)
labels
labels=list(labels)

class Group:
    def __init__(self,labels):
        self.labels=labels
        self.group_num=[0 for i in range(l)]
        for i in labels:
            self.group_num[i]+=1
    def get_group_num(self,i):
        return self.group_num[self.labels[i]]

group=Group(labels)


def get_frend_num(i):
    return frends_num[i]


def make_block(k,n):
    block_num=[0 for i in range(n)]
    for p in range(k):
        i,j =[int(l)-1 for l in input().split()]
        new_i=min(i,j)
        new_j=max(i,j)
        if labels[new_i]==labels[new_j]:
            block_num[i]+=1
            block_num[j]+=1
    return block_num

block=make_block(k,n)

def get_block_num(i):
    return block[i]

ans=[]
for i in range(n):
    ans.append(str(group.get_group_num(i)-1-get_frend_num(i)-get_block_num(i)))
print((" ".join(ans)))

