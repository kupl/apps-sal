arr = [[int(x) for x in input().split()] for i in range(3)]
s = sum((sum(x) for x in arr)) // 2
arr[0][0] = s - sum(arr[0])
arr[1][1] = s - sum(arr[1])
arr[2][2] = s - sum(arr[2])
print('\n'.join((' '.join([str(x) for x in l]) for l in arr)))
