n = int(input())
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
for i in ['M', 'S', 'XS', 'XXS', 'XXXS', 'L', 'XL', 'XXL', 'XXXL']:
    while i in A and i in B:
        del A[A.index(i)]
        del B[B.index(i)]
print(len(A))
