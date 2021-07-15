count = 0
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (numbers[i] + numbers[j]) > numbers[k]:
                if numbers[i] != numbers[j] and numbers[j] != numbers[k]:
                    count += 1
print(count)

