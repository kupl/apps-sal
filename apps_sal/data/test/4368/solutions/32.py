(N, K) = map(int, input().split())
digit = 0
while N > 0:
    N = N // K
    digit += 1
print(digit)
