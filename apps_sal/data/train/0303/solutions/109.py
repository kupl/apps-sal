class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        size = len(arr)
        mem = [0] * size

        for i in range(size):
            mem[i] = arr[i]
            for j in range(0, k):
                if i - j > 0:
                    candidate = max(arr[i - j: i + 1]) * (j + 1) + mem[i - j - 1]
                    mem[i] = max(mem[i], candidate)
                elif i - j == 0:
                    candidate = max(arr[i - j: i + 1]) * (j + 1)
                    mem[i] = max(mem[i], candidate)
                else:
                    break
        return mem[size - 1]

