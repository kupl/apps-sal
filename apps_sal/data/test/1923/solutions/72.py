n = int(input())
array = [int(x) for x in input().split()]
array.sort()
res = 0
for index in range(0, n):
    res += min(array[2 * index], array[2 * index + 1])
print(res)
