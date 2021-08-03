N, A, B = map(int, input().split())

L = []
for i in range(1, N + 1):
    j = map(int, list(str(i)))
    if A <= sum(j) <= B:
        L.append(i)
print(sum(L))
