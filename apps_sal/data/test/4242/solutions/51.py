(A, B, K) = map(int, input().split())
L = []
for i in range(1, 101):
    if A % i == 0 and B % i == 0:
        L.append(i)
print(L[-K])
