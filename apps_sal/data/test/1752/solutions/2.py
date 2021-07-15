n = int(input())
arr = list(map(int, input().split()))

order = [None]* n

arr.sort()

order[0] = arr[0]
for i in range(1, n):
    if (i % 2):
        order[-((i+1)//2)] = arr[i]
    else:
        order[i//2] = arr[i]

print(' '.join(list(map(str, order))))

