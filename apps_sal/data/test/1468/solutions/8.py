n = int(input())
arr = [input() for i in range(n)]

for i in range(n - 1, 0, -1):
    new = arr[i]
    old = arr[i - 1]
    le1 = len(new)
    le2 = len(old)
    for j in range(min(le1, le2)):
        if new[j] < old[j]:
            arr[i - 1] = old[:j]
            break
        elif new[j] > old[j]:
            break
    else:
        if le2 > le1:
            arr[i - 1] = arr[i]


print('\n'.join(arr))
