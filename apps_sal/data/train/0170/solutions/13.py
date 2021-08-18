class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = len(arr)
        if l == 1:
            return 0

        longest = 0

        benchmark = 'a'

        for i in range(1, l):
            if arr[i - 1] > arr[i]:
                head_longest = i
                benchmark = arr[i - 1]
                break

        if benchmark == 'a':
            return 0

        i = l - 2
        if arr[i + 1] >= benchmark:
            head_longest += 1
        while arr[i] <= arr[i + 1] and arr[i] >= benchmark:
            head_longest += 1
            i -= 1

        for i in range(l - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                tail_longest = l - i - 1
                benchmark = arr[i + 1]
                break

        i = 1
        if arr[i - 1] <= benchmark:
            tail_longest += 1

        while arr[i - 1] <= arr[i] and arr[i] <= benchmark:
            tail_longest += 1
            i += 1

        longest = max(head_longest, tail_longest)

        return l - longest
