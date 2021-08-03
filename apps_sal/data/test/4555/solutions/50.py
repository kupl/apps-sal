A, B, K = map(int, input().split())
L = set()
for i in range(A, A + K):
    if i <= B:
        L.add(i)
for i in range(B, B - K, -1):
    if i >= A:
        L.add(i)
print(*sorted(list(L)), sep="\n")
