N, K = map(int, input().split())
h = map(int, input().split())
ride = 0

for cm in h:
    if cm >= K:
        ride = ride + 1
    else:
        continue

print(ride)
