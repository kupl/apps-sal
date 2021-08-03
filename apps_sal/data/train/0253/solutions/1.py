class Solution:
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        length = len(machines)
        if total % length != 0:
            return -1

        avg = int(total / length)
        cum = 0
        target = 0
        result = 0
        for m in machines:
            cum += m
            target += avg
            max_share = m - avg  # example [0,3,0] 3 must output 1 to one side at a time, so it needs 2 steps: one for each side.
            result = max(result, abs(target - cum), max_share)
            # When cum-target<0, it means right side must transfer abs(cum-target) to the left side
            # example: [0, 0, 11, 5], avg=4, at the second 0, cum=0, target=2*avg=8, we need to transfer 8-0=8 to the left side
            # the second 0 is the only interface to the right side, so the right side need 8 steps to fill the left side

            # When cum-target>0, it means left side must transfer abs(cum-target) to the right side
            # example: [4,3,2,1,0], avg=2, at 3, cum=7, target=2*avg=4, we need to transfer 7-4=3 to the right side
            # 3 is the only interface to the right side, so the left side need 3 steps to fill the right side
        return result
