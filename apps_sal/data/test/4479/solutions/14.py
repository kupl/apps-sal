class Solution:

    def largestSumAfterKNegations(self, arr: List[int], k: int) -> int:
        ra = k
        arr.sort()
        for _ in range(ra):
            for j in range(len(arr)):
                if arr[j] < 0:
                    arr[j] = abs(arr[j])
                    k -= 1
                    arr.sort()
                    break
                elif arr[j] == 0:
                    return sum(arr)
                elif k % 2 == 0:
                    return sum(arr)
                else:
                    arr.sort()
                    arr[0] = -arr[0]
                    return sum(arr)
        return sum(arr)
