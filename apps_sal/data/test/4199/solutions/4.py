(N, K) = map(int, input().split())
height = list(map(int, input().split()))
availability = 0
for i in range(0, N):
    if height[i] >= K:
        availability += 1
print(availability)
