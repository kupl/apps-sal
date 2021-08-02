N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
list1 = []
ame = A[0]
for i in range(N - 1):
    list1.append(sum(A[:i + 1]) + sum(B[i:]))

if list1 == []:
    print(A[0] + B[0])
else:
    print(max(list1))
