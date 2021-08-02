N, K = list(map(int, input().split()))
l = []

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    l.extend(A)

print((N - len(set(l))))
