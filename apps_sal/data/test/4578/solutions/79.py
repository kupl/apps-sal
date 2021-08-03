N, X = list(map(int, input().split()))

m = []

for i in range(N):
    m.append(int(input()))

print(((X - sum(m)) // min(m) + N))
