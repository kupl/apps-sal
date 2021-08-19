class Solution:

    def minDays(self, n: int) -> int:
        (queue, steps) = ([n], 0)
        appears = dict()
        while queue:
            n_queue = []
            for ele in queue:
                appears[ele] = 1
            for ele in queue:
                if ele < 2:
                    return steps + ele
                if ele - 1 not in appears:
                    n_queue.append(ele - 1)
                if ele % 2 == 0 and ele / 2 not in appears:
                    n_queue.append(ele // 2)
                if ele % 3 == 0 and ele / 3 not in appears:
                    n_queue.append(ele // 3)
            steps += 1
            queue = n_queue
        return steps
