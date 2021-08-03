N, K = list(map(int, input().split()))

i = 1
while N // K >= 1:
    N = N // K
    i += 1

print(i)
