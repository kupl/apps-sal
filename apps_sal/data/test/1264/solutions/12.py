n = int(input())
numbers = list(map(int, input().split()))
cnt = numbers.count(1)
MAX = 0

for i in range(n):
    for j in range(i, n):
        MAX = max(MAX, cnt + (j - i + 1) - 2 * sum(numbers[i:j + 1]))
print(MAX)
