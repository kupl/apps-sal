A, B, K = map(int, input().split())

L = []
s = [i for i in range(A, min(A + K, B + 1))]
l = [j for j in range(B, max(A - 1, B - K), -1)]
L += s + l
L = list(set(L))
L.sort()

for i in L:
    print(i)
