N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()

if N % 2 == 1:
    Amed = A[N // 2]
    Bmed = B[N // 2]
    print(Bmed - Amed + 1)
else:
    Amed = (A[N // 2] + A[N // 2 - 1]) / 2
    Bmed = (B[N // 2] + B[N // 2 - 1]) / 2
    print(round((Bmed - Amed) * 2 + 1))
