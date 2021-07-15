N = int(input())
numbers = {}
for i in range(N):
    x = int(input())
    if x in numbers:
        del numbers[x]
    else:
        numbers[x] = 1
print(len(numbers))
