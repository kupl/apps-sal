N = int(input())
X = list(map(int, input().split()))
min = 100 * 10000
for p in range(100):
    sum = 0
    for i in X:
        sum += (i - p) ** 2
    if sum < min:
        min = sum
print(min)
