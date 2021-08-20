def LS():
    return list(input().split())


(A, B) = LS()
A = int(A)
B = B.replace('.', '', 1)
B = int(B)
ans = A * B
ans //= 100
print(ans)
