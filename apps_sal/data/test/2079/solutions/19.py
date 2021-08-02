# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, temp, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L1 = [0] * n1
    L2 = [0] * n1
    R1 = [0] * n2
    R2 = [0] * n2
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L1[i] = arr[l + i]
        L2[i] = temp[l + i]
    for j in range(0, n2):
        R1[j] = arr[m + 1 + j]
        R2[j] = temp[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

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

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L1[i]
        temp[k] = L2[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R1[j]
        temp[k] = R2[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, temp, l, r):
    if l < r:

        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, temp, l, m)
        mergeSort(arr, temp, m + 1, r)
        merge(arr, temp, l, m, r)


# Driver code to test above
n = int(input())
arr = list(map(int, input().split()))
temp = []
for i in range(n):
    temp.append(i + 1)
j = 0
k = -1
arrx = [0] * n
mergeSort(arr, temp, 0, n - 1)
# print(temp[i],temp1[temp[i]])
# print(temp1)
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
    # print(j,k)
print(' '.join(map(str, arry)))
