(H, A) = list(map(int, input().split()))
if H % A == 0:
    print(H // A)
else:
    print(H // A + 1)
