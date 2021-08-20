class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        counts = [count for (number, count) in counts.most_common()]
        set_size = 0
        tot = 0
        for x in counts:
            tot += x
            set_size += 1
            if tot >= len(arr) // 2:
                break
        return set_size
