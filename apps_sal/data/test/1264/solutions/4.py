n = int(input())
numbers = list(map(int, input().split()))
count_1 = numbers.count(1)
Max = 0
for i in range(n):
    for j in range(i, n):
        Max = max(Max, count_1 + (j - i + 1) - 2 * sum(numbers[i:j + 1]))
print(Max)
