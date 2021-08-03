N, K = map(int, input().split())
sweets = [0] * N

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))

    for a in A:
        sweets[a - 1] += 1

print(sweets.count(0))
