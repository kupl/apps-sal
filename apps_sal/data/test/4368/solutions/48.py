N, K = list(map(int, input().split()))

ans = 0

while N >= K:
    N = N // K
    ans += 1

print((ans + 1))
