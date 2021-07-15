N, K = map(int, input().split())
h = list(map(int, input().split()))

person = 0

for i in range(0, N):
    if h[i] >= K:
        person += 1

print(person)
