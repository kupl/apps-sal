N = int(input())
(D, X) = list(map(int, input().split()))
A = [int(input()) for _ in range(N)]
c = sum(((D - 1) // a + 1 for a in A))
print(X + c)
