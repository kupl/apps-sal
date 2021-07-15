N = int(input())
A = sorted(list(map(int,input().split())))
B = A[-1]
print(B,min(A,key=lambda x: abs(B-2*x)))
