n = int(input())
A = sorted(list(map(int, input().split())))
print(A[-1], ' '.join(map(str, A[1:-1])), A[0])
