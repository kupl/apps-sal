n = int(input())
a = list(map(int, input().split()))
num_drink = int(input())

for i in range(num_drink):
    P,X = map(int,input().split())
    A = a.copy()
    A[P-1] = X
    print(sum(A))
