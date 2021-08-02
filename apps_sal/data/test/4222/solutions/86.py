N, K = map(int, input().split())

treat = [0] * N

for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        treat[a - 1] += 1

print(treat.count(0))
