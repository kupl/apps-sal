N = int(input())
S = input()[::-1]
x = int(S, 2) + 1
Sp = bin(x)[2:].zfill(N)[-N:]
print(sum(a != b for a, b in zip(S, Sp)))

