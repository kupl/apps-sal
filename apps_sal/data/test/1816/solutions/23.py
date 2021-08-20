n = int(input())
location = {int(val): i for (i, val) in enumerate(input().split())}
result = sum((abs(location[i] - location[i - 1]) for i in range(2, n + 1)))
print(result)
