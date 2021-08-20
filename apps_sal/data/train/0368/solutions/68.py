def merge(arr1, arr2):
    (index1, index2) = (0, 0)
    res = []
    while index1 < len(arr1) or index2 < len(arr2):
        if index1 >= len(arr1) or (index2 < len(arr2) and arr1[index1] > arr2[index2]):
            res.append(arr2[index2])
            index2 += 1
        else:
            res.append(arr1[index1])
            index1 += 1
    return res


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    m = int(len(arr) / 2)
    return merge(mergeSort(arr[:m]), mergeSort(arr[m:]))


def splitAtZero(sortedArr):
    for i in range(len(sortedArr)):
        if sortedArr[i] >= 0:
            return (sortedArr[:i], sortedArr[i:])
    return (sortedArr, [])


def coefficient(arr):
    res = 0
    for i in range(len(arr)):
        res += (i + 1) * arr[i]
    return res


class Solution:

    def maxSatisfaction(self, unsortedSatisfaction: List[int]) -> int:
        satisfaction = mergeSort(unsortedSatisfaction)
        runningSum = 0
        for i in reversed(list(range(len(satisfaction)))):
            runningSum += satisfaction[i]
            if runningSum <= 0:
                return coefficient(satisfaction[i + 1:])
        return coefficient(satisfaction)
