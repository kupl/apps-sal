class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        queue = deque([arr[-1]])
        for i in range(len(arr) - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                break
            queue.appendleft(arr[i - 1])

        if len(queue) == len(arr):
            return 0

        l = len(arr) - len(queue)

        def search(target):
            lo = l
            hi = l + len(queue)

            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        curMin = len(arr) - len(queue)
        i = 0
        while i < len(arr) - 1 and arr[i] <= arr[i + 1]:
            idx = search(arr[i])
            curMin = min(idx - i - 1, curMin)
            i += 1
        idx = search(arr[i])
        curMin = min(idx - i - 1, curMin)

        return curMin
