(K, S) = list(map(int, input().split()))
count = 0
for i in range(K + 1):
    for j in range(K + 1):
        if S - i - j <= K and S - i - j >= 0:
            count += 1
print(count)
