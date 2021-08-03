N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

N -= 1
i = 1
koko = A[0]
f = 0
while 1:
    for _ in range(2):
        N -= 1
        if N == 0:
            f = 1
            break
        koko += A[i]
    if f == 1:
        break
    i += 1
print(koko)
