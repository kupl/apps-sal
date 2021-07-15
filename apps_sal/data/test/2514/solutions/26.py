N = int(input())
A= [0]*110000
sum = 0
for i in map(int, input().split()):
    sum += i
    A[i] += 1
    
Q = int(input())
for i in range(Q):
    B,C = map(int,input().split())
    sum += (C-B)*A[B]
    A[C] += A[B]
    A[B] = 0
    print(sum)
