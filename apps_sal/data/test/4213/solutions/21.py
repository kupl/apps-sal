N = int(input())
A = [int(a) for a in input().split()]
lists = [abs(A[i] - A[j]) for i in range(N) for j in range(N)]
print(max(lists))
