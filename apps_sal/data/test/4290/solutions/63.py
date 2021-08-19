inp = input().split()
n = int(inp[0])
m = int(inp[1])
arr = []
pares = 0
impares = 0
count = 1
nums = 0


def binary(arr, menor, mayor, x):
    if mayor >= menor:
        med = (mayor + menor) // 2
        if arr[med] == x:
            return med
        elif arr[med] > x:
            return binary(arr, menor, med - 1, x)
        else:
            return binary(arr, med + 1, mayor, x)
    else:
        return -1


while len(arr) < m + n:
    if count % 2 == 0 and pares < n:
        arr.append(count)
        pares += 1
    elif count % 2 != 0 and impares < m:
        arr.append(count)
        impares += 1
    count += 1
sums = []
for x in arr:
    for y in arr:
        if (x + y) % 2 == 0 and binary(sums, 0, len(sums) - 1, [y, x]) == -1 and (x != y):
            sums.append([x, y])
            nums += 1
print(nums)
