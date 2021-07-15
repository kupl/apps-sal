N, K = list(map(int, input().split()))

h = []
for i in range(N):
    h.append(int(input()))
    
h.sort()
h.reverse()

ls = []

for i in range(N - K + 1):
    ls.append(h[i] - h[i + K - 1])

print((min(ls)))

