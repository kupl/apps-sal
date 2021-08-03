
def findIndex(arr, ele, start, end):

    while (start < end):
        middle = (start + end - 1) // 2

        if ele == arr[middle]:
            return middle
        if ele < arr[middle]:
            end = middle
        elif ele > arr[middle]:
            start = middle + 1

    return -1


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        temp, total = 0, 0
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        path1, path2 = nums1, nums2

        while (i < n1):
            index = findIndex(path2, path1[i], j, n2)
            if index == -1:
                total += path1[i]
                temp += path1[i]
                i += 1
            else:
                if (temp >= sum(path2[j: index])):
                    total += path1[i]
                    temp = path1[i]
                else:
                    total -= temp
                    total += sum(path2[j: index + 1])
                    temp = path2[index]
                i, j = index + 1, i
                n1, n2 = n2, n1
                path1, path2 = path2, path1

        if (temp < sum(path2[j: n2])):
            total -= temp
            total += sum(path2[j: n2])
        return (total % 1000000007)
