class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        pending_on = set()
        already_on = set()
        count = 0
        for (idx, lgt) in enumerate(light):
            lgt -= 1
            if idx in already_on:
                already_on.remove(idx)
            else:
                pending_on.add(idx)
            if lgt in pending_on:
                pending_on.remove(lgt)
            else:
                already_on.add(lgt)
            if len(pending_on) == 0:
                count += 1
        return count
