N, A, B = list(map(int, input().split()))

D = []

den = N * A
D.append(den)

D.append(B)

D.sort()

print((D[0]))
