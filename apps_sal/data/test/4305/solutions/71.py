(H, N) = map(int, input().split())
a = H // N
if H % N != 0:
    a += 1
print(a)
