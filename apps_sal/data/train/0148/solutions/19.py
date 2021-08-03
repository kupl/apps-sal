class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if difficulty is None:
            return 0
        thislist = []
        for i in range(0, len(difficulty)):
            thislist.append((difficulty[i], profit[i]))
        thislist.sort()
        worker.sort()
        res = 0
        curr_max = 0
        worker_index = 0
        list_index = 0
        while worker_index < len(worker) and list_index < len(thislist):
            if thislist[list_index][0] <= worker[worker_index]:
                curr_max = max(curr_max, thislist[list_index][1])
                list_index += 1
            else:
                res += curr_max
                worker_index += 1

        if worker_index < len(worker):
            res += curr_max * (len(worker) - worker_index)
        return res
