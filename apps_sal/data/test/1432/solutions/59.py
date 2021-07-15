N = int(input())
A = list(map(int, input().split()))
x = 0
for i in A:
    x = i-x
print(x, end=" ")
x//=2
for i in range(N-1):
    x = A[i]-x
    print(2*x, end=" ")

