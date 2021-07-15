from collections import deque
n = int(input())
A = list(map(int, input().split()))
B = deque()

for i in range(n):
    if i%2 == 0:
        B.append(A[i])
    else:
        B.appendleft(A[i])
B = list(B)        
if n%2 != 0:
    B = B[::-1]
print((*B))


