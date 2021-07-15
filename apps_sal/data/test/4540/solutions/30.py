N = int(input())
A = [int(x) for x in input().split()]
A.insert(0,0)
A.append(0)
cost = 0
for i in range(1,N+2):
    cost += abs(A[i]-A[i-1])

def change(i):
    nonlocal A
    return -abs(A[i+1]-A[i])-abs(A[i]-A[i-1])+abs(A[i+1]-A[i-1])

for i in range(1,N+1):
    print(cost+change(i))
