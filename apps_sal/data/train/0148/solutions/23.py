class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:

        pairs = [(a, b) for a, b in zip(difficulty, profit)]
        sorted_pairs = sorted(pairs, key=lambda p: p[0])
        benifit = []
        current_max = 0
        for diff, pro in sorted_pairs:
            current_max = max(pro, current_max)
            benifit.append((diff, current_max))

        sorted_workers = sorted(worker)
        ans = 0
        current_difficulty_index = worker_index = 0
        while worker_index < len(worker):
            if sorted_workers[worker_index] < benifit[current_difficulty_index][0]:
                worker_index += 1
                continue
            while (
                current_difficulty_index + 1 < len(worker) and
                benifit[current_difficulty_index + 1][0] <=
                sorted_workers[worker_index]
            ):
                current_difficulty_index += 1

            ans += benifit[current_difficulty_index][1]
            worker_index += 1

        return ans
