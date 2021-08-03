H, A = [int(n) for n in input().split()]
print(H // A if H % A == 0 else H // A + 1)
