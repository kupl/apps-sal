

def isPossibleDivide(nums, k):
    if (len(nums) % k != 0):
        return False
    else:
        nums.sort()
        return decreaseConquer(nums, k)


def decreaseConquer(A, k):
    if (len(A) == 0):
        return True
    else:
        pivot = A[len(A) - 1]
        for i in range(k):
            j = binarySearch(A, 0, len(A) - 1, pivot - i)
            if (j == -1):
                return False
            else:
                del A[j]
        return decreaseConquer(A, k)


def binarySearch(S, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2

        if S[mid] == x:
            return mid

        elif S[mid] > x:
            return binarySearch(S, l, mid - 1, x)

        else:
            return binarySearch(S, mid + 1, r, x)

    else:
        return -1


A = [1, 2, 3, 3, 4, 4, 5, 6]
k = 4
ans = isPossibleDivide(A, k)

print(ans)


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        return isPossibleDivide(nums, k)
