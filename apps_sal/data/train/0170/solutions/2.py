class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        stack = [0]
        stack2 = []
        total = 0
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                stack.append(0)
            else:
                total += 1
                stack2.append(i)
                stack.append(1)
        if total == 0:
            return 0
        print(stack2)
        # erase small

        def erase(i, j):
            print((i, j))
            if (i > 0 and j < len(arr) - 1) and arr[i - 1] > arr[j + 1]:
                return min(erase(i - 1, j), erase(i, j + 1))

            else:
                return j - i + 1

        if total == 1:
            return erase(stack2[0], stack2[0])

        return erase(stack2[0], stack2[-1] - 1)
