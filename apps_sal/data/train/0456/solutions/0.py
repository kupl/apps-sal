class Solution:

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones == []:
            return False
        if len(stones) == 1:
            return True
        diff = [0] * len(stones)
        for i in range(1, len(stones)):
            if stones[i] - stones[i - 1] > i:
                return False
        stk = [(0, 0)]
        dictt = {}
        for (idx, stone) in enumerate(stones):
            dictt[stone] = idx
        while stk:
            (idx, prevjump) = stk.pop()
            for k in range(max(1, prevjump - 1), prevjump + 2):
                if stones[idx] + k in dictt:
                    x = dictt[stones[idx] + k]
                    if x == len(stones) - 1:
                        return True
                    stk.append((dictt[stones[idx] + k], k))
        return False
