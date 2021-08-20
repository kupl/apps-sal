class Solution:

    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        (profit, people, res, board) = (0, 0, 0, 0)
        minPeople = runningCost // boardingCost
        if sum(customers) < minPeople:
            return -1
        for n in customers:
            people += n
            res += 1
            if people >= 4:
                people -= 4
                board += 4
            else:
                board += people
                people = 0
        (count, m) = divmod(people, 4)
        board += count * 4
        if m > minPeople:
            count += 1
            board += m
        res += count
        profit += board * boardingCost - res * runningCost
        return res if profit >= 0 else -1
