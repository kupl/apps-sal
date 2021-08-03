N, K = list(map(int, input().split()))
Speeds = list(map(int, input().split()))
Speeds.sort()
print(Speeds[-K])
