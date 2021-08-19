class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        size = len(jobDifficulty)
        memoi = [jobDifficulty[0]] * size
        for i in range(1, size):
            memoi[i] = max(memoi[i - 1], jobDifficulty[i])
        maxes = {(0, i): memoi[i - 1] for i in range(1, size + 1)}

        def findMax(s, e):
            return maxes.setdefault((s, e), max(jobDifficulty[s:e]))
        for cut in range(1, d):
            newMemoi = [float('inf')] * size
            for end in range(cut, size):
                for split in range(cut - 1, end):
                    newMemoi[end] = min(newMemoi[end], memoi[split] + findMax(split + 1, end + 1))
            memoi = newMemoi
        return memoi[-1] if memoi[-1] != float('inf') else -1
