class Solution:

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        from collections import Counter
        counter = Counter(tasks)
        window = n + 1
        biggest_freq = max(list(counter.values()))
        num_of_max_freq = list(counter.values()).count(biggest_freq)
        return max(window * (biggest_freq - 1) + num_of_max_freq, len(tasks))
