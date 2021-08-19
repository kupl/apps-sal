(N, M, X) = map(int, input().split())
A = sum((int(i) < X for i in input().split()))
print(min(A, M - A))
