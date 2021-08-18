
N, S = list(map(int, input().split()))

arrivals = [0 for i in range(S + 1)]
for i in range(N):
    f, t = list(map(int, input().split()))
    arrivals[f] = max(arrivals[f], t)

for i in range(S, 0, -1):
    arrivals[i - 1] = max(arrivals[i - 1], arrivals[i] + 1)
print(arrivals[0])
