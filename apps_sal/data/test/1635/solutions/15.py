n = int(input())
numbers = list(map(int, input().split()))
last = dict()
for i in set(numbers):
    last[i] = 0
for i in range(n):
    last[numbers[i]] = i
print(min(list(last.items()), key=lambda x: x[1])[0])
