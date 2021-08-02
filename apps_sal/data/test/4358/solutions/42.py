N = int(input())
P = sorted(list(int(input()) for _ in range(N)), reverse=True)
P[0] = int(P[0] * .5)
print((sum(P)))
