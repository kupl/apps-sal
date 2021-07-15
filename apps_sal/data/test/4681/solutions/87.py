
N = int(input())
L = [2, 1]
if N == 1:
    print(1)
    return

for i in range(2, N+1):
    L[i % 2] = sum(L)
print(L[N % 2])
