N, K, M = [int(n) for n in input().split()]
A = sum([int(n) for n in input().split()])

score = N * M - A
if score <= K:
    print(max(0, score))
else:
    print(-1)
