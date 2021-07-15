n = int(input())

nulls = 0
head = '1'

for number in input().rstrip().split():
    i = 0
    if number[0] == '0':
        print(0)
        break
    for digit in number:
        if digit not in ('0', '1') or (digit == '1' and i > 0):
            head = number
            break
        i += 1
    else:
        nulls += len(number) - 1
else:
    print(head + '0' * nulls)
