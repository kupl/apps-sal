class Solution:

    def minDays(self, n: int) -> int:
        (queue, steps) = ([n], 0)
        appears = dict()
        while queue:
            n_queue = []
            for k in range(len(queue) - 1, -1, -1):
                appears[queue[k]] = 1
                if queue[k] < 2:
                    return steps + queue[k]
                if queue[k] - 1 not in appears:
                    n_queue.append(queue[k] - 1)
                if queue[k] % 2 == 0 and queue[k] / 2 not in appears:
                    n_queue.append(queue[k] // 2)
                if queue[k] % 3 == 0 and queue[k] / 3 not in appears:
                    n_queue.append(queue[k] // 3)
            steps += 1
            queue = n_queue
        return steps
