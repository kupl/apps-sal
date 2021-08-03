def isPossibleDivide(nums, k):
    if (len(nums) % k != 0):  # if the size of arrays is not divisible by k, cannot have sets of k numbers
        return False
    else:
        nums.sort()  # sort array
        return decreaseConquer(nums, k)  # calling the decrease/conquer algorihtm with the sorted array.

# Decrease-Conquer algorithm to determine if array can be divide into sets of k consecutive numbers


def decreaseConquer(A, k):
    if (len(A) == 0):  # base case
        return True
    else:  # recursive
        pivot = A[len(A) - 1]  # choose the last element (the largest element) in array
        for i in range(k):  # search for k consecutives in correspond to the largest number
            j = binarySearch(A, 0, len(A) - 1, pivot - i)  # use binary search to find p-1, p-2,.., p-(k-1)
            if (j == -1):  # if element is not found in the array, there is no k consecutive numbers
                return False
            else:  # if found, remove the element from array
                del A[j]
        # array is reduced in size (n - k), recursively calling decreaseConquer algorithm with the updated array
        return decreaseConquer(A, k)

# Search for specific element in the array - O(log n)


def binarySearch(S, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2  # find the middle element

        if S[mid] == x:  # If element is the middle element
            return mid

        elif S[mid] > x:  # if element is in the left subarray
            return binarySearch(S, l, mid - 1, x)

        else:  # if element is in the right subarray
            return binarySearch(S, mid + 1, r, x)

    else:  # Element is not present in the array
        return -1


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        return isPossibleDivide(nums, k)
