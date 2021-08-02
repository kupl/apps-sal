K, S = list(map(int, input().split()))
Sum = 0

for i in range(K + 1):
    for j in range(K + 1):
        if 0 <= S - i - j <= K:
            Sum += 1

print(Sum)
