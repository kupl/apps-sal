N, A, B = map(int, input().split())

r = N // (A + B) * A
s = N % (A + B)

x = r + min(A, s)
print(x)
