import numpy as np

def isPrimeNum(x):
    if type(x) is not int: return False
    if x <= 1: return False
    if x <= 3: return True
    max = int(np.sqrt(x))
    for i in range(2, max+1):
        if x % i == 0: return False
    return True
    
def isNumLike2017(x):
    if isPrimeNum(x) == False: return False
    if isPrimeNum(int((x+1)/2)) == False: return False
    return True
        
N = 10**5
X = np.zeros(N, dtype='int64')
for i in range(1, N+1):
    if isNumLike2017(i): X[i-1] += 1
X = X.cumsum()

Q = int(input())
for _ in range(Q):
    l, r = input().split()
    l, r = int(l), int(r)
    if l == 1: L = 0
    else: L = X[l-2]
    R = X[r-1]
    print(R - L)
