N = int(input())
D = list(map(int, input().split()))
D = sorted(D)
c = (N // 2) - 1
A = D[N // 2] - D[c]
print(A)
