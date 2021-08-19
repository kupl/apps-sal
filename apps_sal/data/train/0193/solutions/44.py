class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        cnter = collections.Counter(arr).most_common()
        counting = 0
        for (i, blep) in enumerate(cnter):
            if counting + blep[1] >= len(arr) / 2:
                return i + 1
            else:
                counting += blep[1]
