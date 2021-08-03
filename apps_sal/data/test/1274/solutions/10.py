def insertHeap(array, val):
    array.append(val)
    n = len(array) - 1
    while n != 0:
        parent = int((n - 1) / 2)
        if array[n] > array[parent]:
            tmp = array[n]
            array[n] = array[parent]
            array[parent] = tmp
            n = parent
        else:
            break
    return array


def desertHeap(array):
    if array == []:
        return None
    array[0], array[-1] = array[-1], array[0]
    res = array.pop(-1)
    n = len(array)
    if n == 0 or n == 1:
        return res
    parent = 0
    while True:
        child = 2 * parent + 1
        if child >= n:
            break
        if (child + 1 < n) and array[child] < array[child + 1]:
            child += 1
        if array[parent] < array[child]:
            array[child], array[parent] = array[parent], array[child]
            parent = child
        else:
            break
    return res


n, m = map(int, input().split())

li = [[] for j in range(10**5 + 1)]

for _ in range(n):
    a, b = map(int, input().split())
    li[a].append(b)

ans = 0
jobsHeap = []
for i in range(1, m + 1):
    for val in li[i]:
        jobsHeap = insertHeap(jobsHeap, val)

    if jobsHeap != []:
        res = desertHeap(jobsHeap)
        ans += res
print(ans)
