class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        arr = []
        for i in range(len(profit)):
            arr.append([difficulty[i], profit[i]])
        arr.sort(key=lambda x: x[0])
        for i in range(len(arr)):
            difficulty[i] = arr[i][0]
            profit[i] = arr[i][1]
        prev = [profit[0]]
        for i in range(1, len(profit)):
            prev.append(max(profit[i], prev[-1]))
        i = 0
        p = 0
        j = 0
        while j < len(worker):
            if i == len(difficulty):
                p += prev[i - 1]
                j += 1
                continue
            if difficulty[i] <= worker[j]:
                i += 1
            else:
                x = i - 1
                while x >= 0 and difficulty[x] > worker[j]:
                    x -= 1
                if x >= 0:
                    p += prev[x]
                j += 1
        return p
