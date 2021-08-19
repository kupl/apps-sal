"""
Created on Wed Sep 16 12:35:58 2020

@author: liang
"""
(N, M) = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort(reverse=True)
count = 0
while count != M:
    A[0] //= 2
    count += 1
    tmp = A[0]
    for i in range(1, N):
        if count == M:
            break
        if A[i] > tmp:
            A[i] //= 2
            count += 1
    A.sort(reverse=True)
ans = sum(A)
print(ans)
