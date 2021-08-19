(N, A, B) = map(int, input().split())
s = A + B
print(N // s * A + min(N % s, A))
