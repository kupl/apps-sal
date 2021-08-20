def wheel(cust, ticket, cost):
    n_waiting = 0
    earn = 0
    rots = 0
    res = [0, 0]
    i = 0
    l = len(cust)
    while True:
        if i < l:
            n_waiting += cust[i]
            i += 1
        seated = min(n_waiting, 4)
        if i == l and seated == 0:
            break
        n_waiting -= seated
        earn += seated * ticket - cost
        rots += 1
        if earn > res[1]:
            res[1] = earn
            res[0] = rots
    if res[0] <= 0:
        return -1
    return res[0]


class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        return wheel(customers, boardingCost, runningCost)
