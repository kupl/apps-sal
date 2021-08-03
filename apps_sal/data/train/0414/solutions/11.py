class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) - 1:
            return max(arr)
        od = OrderedDict()
        for n in arr:
            od[n] = True
        wins = 0
        prev, _ = od.popitem(last=False)
        while True:
            cur, _ = od.popitem(last=False)
            if prev > cur:
                wins += 1
                od[cur] = True
            else:
                prev = cur
                wins = 1
                od[prev] = True
            if wins == k:
                break
        return prev
