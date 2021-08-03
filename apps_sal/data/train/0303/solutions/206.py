class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        size = len(arr)
        mem = [0] * size

        for i in range(size):
            maxArr = 0
            for j in range(0, k):
                if i - j >= 0:
                    maxArr = max(maxArr, arr[i - j])
                    candidate = maxArr * (j + 1)
                    candidate += 0 if i - j == 0 else mem[i - j - 1]
                    mem[i] = max(mem[i], candidate)
                else:
                    break
        return mem[size - 1]
