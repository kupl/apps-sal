H, N = map(int, input().split())

if H % N == 0:
    print(H//N)
elif H % N != 0:
    print(H // N + 1)
