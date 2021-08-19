class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        if len(arr) < 3:
            return 1

        counter = {}  # Could use defaultdict to save a few lines of code
        for n in arr:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        counts = sorted(counter.values())

        total_ints = len(arr)
        set_size = 0

        while total_ints > len(arr) // 2:
            set_size += 1
            total_ints -= counts.pop()

        return set_size
