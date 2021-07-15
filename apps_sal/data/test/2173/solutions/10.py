i = int(input())
values = list(map(int, input().split(' ')))
result = [-1] * i
sortedValues = sorted(range(i), key=lambda x: values[x])

cnt = 0
for i in sortedValues:
    cnt = cnt + 1 if cnt + 1 >= values[i] else values[i]
    result[i] = cnt

print(' '.join([str(x) for x in result]))
