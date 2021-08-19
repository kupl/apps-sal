(N, D) = list(map(int, input().split()))
gard = D * 2 + 1
print((int(N / gard), int(N / gard) + 1)[N % gard != 0])
