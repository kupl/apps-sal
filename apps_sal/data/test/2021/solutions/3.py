a = int(input())
A = list(map(int, input().split()))
b = int(input())
B = list(map(int, input().split()))
num = sum(A)
A.sort(reverse=True)
for elem in B:
    print(num - A[elem - 1])
