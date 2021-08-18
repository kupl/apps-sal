N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

possible = []

for i in h:
    if i >= K:
        possible.append(i)

print((len(possible)))
