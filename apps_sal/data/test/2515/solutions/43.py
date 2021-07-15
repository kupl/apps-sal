import numpy as np
from math import sqrt

def main():
    with open(0) as f:
        Q = int(f.readline())
        Query = [tuple(map(int, line.split())) for line in f.readlines()]
    
    p_table = makePtable(10**5)
    p_set = set(p_table)
    Like2017 = [p for p in p_table if (p+1)//2 in p_set]
    #データベースを累積和で作成
    database = np.array([0] * (10**5+1))
    for i in Like2017:database[i] = 1
    database = database.cumsum(axis=0)
    
    for l,r in Query:
        print(database[r+1] - database[l-1])

def makePtable(N):
    table = list(range(2,N+1))
    result = []
    p = 2
    while p < sqrt(N):
        p = table[0]
        result.append(p)
        table = [x for x in table if x % p != 0]
    return result + table

main()
