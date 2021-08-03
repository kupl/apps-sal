n, k = [int(x) for x in input().split()]
numbers = input().split()

result = 0
for number in numbers:
    count = 0
    for x in number:
        if x == '4' or x == '7':
            count += 1
    if count <= k:
        result += 1

print("%d" % result)
