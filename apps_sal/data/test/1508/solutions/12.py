N = int(input())
A = sorted(list(map(int, input().split())))
A[0], A[-1] = A[-1], A[0]
for x in A:
    print(x, end=" ")
