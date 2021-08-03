N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

i = N
count = 0

if N == K:
    count = 1

else:
    while True:
        count += i // K
        i = i // K + i % K
        if i <= K:
            break
    count += 1

print(count)
