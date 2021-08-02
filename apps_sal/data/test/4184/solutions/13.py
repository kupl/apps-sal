N = int(input())
W = list(map(int, input().split()))

m = 10**10
for i in range(1, N):
    m = min(m, abs(sum(W[:i]) - sum(W[i:])))

print(m)
