n = int(input())
a = list(map(int, input().split()))

def findMinimumL(a):
    A = [-1]*len(a)
    for i,x in enumerate(a):
        j = i - 1 
        while j != -1 and a[j] > a[i]:
            j = A[j]
        A[i] = j
    return A

def findMaximumL(a):
    A = [-1]*len(a)
    for i,x in enumerate(a):
        j = i - 1 
        while j != -1 and a[j] < a[i]:
            j = A[j]
        A[i] = j
    return A

def findMinimumR(a):
    A = [-1]*len(a)
    for i in range(len(a) - 1,-1,-1):
        j = i + 1
        while j != len(a) and a[j] >= a[i]:
            j = A[j]
        A[i] = j
    return A

def findMaximumR(a):
    A = [-1]*len(a)
    for i in range(len(a) - 1,-1,-1):
        j = i + 1
        while j != len(a) and a[j] <= a[i]:
            j = A[j]
        A[i] = j
    return A

def minimumSum():
    L,R = findMinimumL(a), findMinimumR(a)
    ans = 0
    for i,x in enumerate(a):
        ans += (i - L[i])*(R[i] - i)*x
    return ans

def maximumSums():
    L,R = findMaximumL(a), findMaximumR(a)
    ans = 0
    for i,x in enumerate(a):
        ans += (i - L[i])*(R[i] - i)*x
    return ans

print(maximumSums() - minimumSum())


