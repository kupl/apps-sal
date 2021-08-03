class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        stack = []
        record = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while len(stack) > 0 and arr[i] > arr[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                record[i] = stack[-1]
            stack.append(i)
        for i in range(len(record)):
            if i == 0:
                if record[i] - i - 1 >= k or record[i] < 0:
                    return arr[i]
            else:
                if record[i] < 0:
                    return arr[i]
                if record[i] - i >= k:
                    return arr[i]
        return -1
