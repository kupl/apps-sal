n = int(input())
numbers = [int(i) for i in input().split()]
i = 1
while i < len(numbers) and numbers[i] >= numbers[i - 1]:
    i += 1
j = len(numbers) - 1
while j > 0 and numbers[j] >= numbers[j - 1]:
    j -= 1
i -= 1
if not j:
    print('yes')
    print(1, 1)
else:
    rev = numbers[i:j + 1]
    rev.reverse()
    sd = numbers[:i] + rev + numbers[j + 1:]
    if sd == sorted(numbers):
        print('yes')
        print(i + 1, j + 1)
    else:
        print('no')
