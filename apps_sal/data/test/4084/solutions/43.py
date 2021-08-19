(N, A, B) = map(int, input().split())
(s, d) = divmod(N, A + B)
print(A * s + min(d, A))
