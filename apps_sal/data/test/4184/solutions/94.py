# ABC129 B

N = int(input())
W = list(map(int, input().split()))
T = []
for t in range(1, N):
    Q = [W[i] for i in range(t)]
    R = [W[i] for i in range(t, N)]
    T.append(abs(sum(Q) - sum(R)))


print((min(T)))
