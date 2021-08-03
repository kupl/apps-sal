N, K = map(int, input().split())
P = [1 for i in range(N)]

for i in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        x = j - 1
        P[x] = 0

print(sum(P))
