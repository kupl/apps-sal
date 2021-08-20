class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        aux = [[0, -1, -1] for _ in range(n)]
        if n == 1:
            return 1 if m == n else -1
        mCounter = 0
        result = -1
        for i in range(n):
            idx = arr[i] - 1
            if idx == 0:
                if aux[idx + 1][0] == m:
                    mCounter -= 1
                aux[idx][0] = aux[idx + 1][0] + 1
                if aux[idx][0] == m:
                    mCounter += 1
                endIdx = idx if aux[idx + 1][2] == -1 else aux[idx + 1][2]
                aux[idx][2] = endIdx
                aux[idx][1] = 0
                aux[endIdx][1] = 0
                aux[endIdx][0] = aux[idx][0]
            elif idx == n - 1:
                if aux[idx - 1][0] == m:
                    mCounter -= 1
                aux[idx][0] = aux[idx - 1][0] + 1
                if aux[idx][0] == m:
                    mCounter += 1
                startIdx = idx if aux[idx - 1][1] == -1 else aux[idx - 1][1]
                aux[idx][1] = startIdx
                aux[idx][2] = n - 1
                aux[startIdx][2] = n - 1
                aux[startIdx][0] = aux[idx][0]
            else:
                if aux[idx - 1][0] == m:
                    mCounter -= 1
                if aux[idx + 1][0] == m:
                    mCounter -= 1
                groupSize = aux[idx + 1][0] + aux[idx - 1][0] + 1
                if groupSize == m:
                    mCounter += 1
                aux[idx][0] = groupSize
                startIdx = idx if aux[idx - 1][1] == -1 else aux[idx - 1][1]
                endIdx = idx if aux[idx + 1][2] == -1 else aux[idx + 1][2]
                aux[idx][1] = startIdx
                aux[idx][2] = endIdx
                aux[startIdx][0] = groupSize
                aux[startIdx][1] = startIdx
                aux[startIdx][2] = endIdx
                aux[endIdx][0] = groupSize
                aux[endIdx][1] = startIdx
                aux[endIdx][2] = endIdx
            if mCounter > 0:
                result = i + 1
        return result
