(number, diameter) = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
numbers.sort()
max_covered = 0
for i in range(len(numbers)):
    j = i
    while j != len(numbers) and abs(numbers[i] - numbers[j]) <= diameter:
        j += 1
    max_covered = max(j - i, max_covered)
print(len(numbers) - max_covered)
