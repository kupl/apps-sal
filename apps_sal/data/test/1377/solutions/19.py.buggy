n = int(input())
array = list(map(int, input().split()))
ind = array.index(max(array))
i, j = ind - 1, ind + 1
now = array[ind]
while i != -1 or j != n:
    if i == -1:
        if array[j] < now:
            now = array[j]
            j += 1
        else:
            print('NO')
            return
    elif j == n:
        if array[i] < now:
            now = array[i]
            i -= 1
        else:
            print('NO')
            return
    else:
        if array[i] > array[j]:
            if array[i] < now:
                now = array[i]
                i -= 1
            else:
                print('NO')
                return
        else:
            if array[j] < now:
                now = array[j]
                j += 1
            else:
                print('NO')
                return
print('YES')
