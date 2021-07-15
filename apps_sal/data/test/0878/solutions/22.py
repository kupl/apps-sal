n = int(input())
arr = [int(x) for x in input().split()]
val = 0
for i in range(n - 1):
    if arr[i] == 2 and arr[i + 1] == 3:
        print('Infinite')
        return
    if arr[i] == 3 and arr[i + 1] == 2:
        print('Infinite')
        return
    if arr[i] == 1 and arr[i + 1] == 2:
        if i > 0 and arr[i - 1] == 3:
            val += 2
        else:
            val += 3
    if arr[i] == 2 and arr[i + 1] == 1:
        val += 3
    if arr[i] == 1 and arr[i + 1] == 3:
        val += 4
    if arr[i] == 3 and arr[i + 1] == 1:
        val += 4
print('Finite')
print(val)

