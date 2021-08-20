(N, A, B) = list(map(int, input().split()))
if N * A < B:
    x = N * A
else:
    x = B
print(x)
