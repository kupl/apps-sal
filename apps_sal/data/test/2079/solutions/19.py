
def merge(arr, temp, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L1 = [0] * n1
    L2 = [0] * n1
    R1 = [0] * n2
    R2 = [0] * n2
    for i in range(0, n1):
        L1[i] = arr[l + i]
        L2[i] = temp[l + i]
    for j in range(0, n2):
        R1[j] = arr[m + 1 + j]
        R2[j] = temp[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L1[i] <= R1[j]:
            arr[k] = L1[i]
            temp[k] = L2[i]
            i += 1
        else:
            arr[k] = R1[j]
            temp[k] = R2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L1[i]
        temp[k] = L2[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R1[j]
        temp[k] = R2[j]
        j += 1
        k += 1


def mergeSort(arr, temp, l, r):
    if l < r:

        m = (l + (r - 1)) // 2

        mergeSort(arr, temp, l, m)
        mergeSort(arr, temp, m + 1, r)
        merge(arr, temp, l, m, r)


n = int(input())
arr = list(map(int, input().split()))
temp = []
for i in range(n):
    temp.append(i + 1)
j = 0
k = -1
arrx = [0] * n
mergeSort(arr, temp, 0, n - 1)
s = str(input())
arry = [0] * len(s)
arrn = [0]
for i in range(len(s)):
    if(s[i] == '0'):
        arry[i] = temp[j]
        arrx[temp[j] - 1] += 1
        arrn.append(temp[j])
        j += 1

    if(s[i] == '1'):
        arry[i] = arrn[-1]
        del arrn[-1]
print(' '.join(map(str, arry)))
