class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        l = list()
        num_of_people = 0
        wait_people = 0
        c = 0
        for i in customers:
            c += 1
            if (i + wait_people) >= 4:
                num_of_people += 4
                wait_people = i + wait_people - 4
            else:
                num_of_people += i + wait_people
                wait_people = 0
            temp = num_of_people * boardingCost - c * runningCost
            l.append(temp)
        while(wait_people > 0):
            c += 1
            if wait_people >= 4:
                num_of_people += 4
                wait_people -= 4
            else:
                num_of_people += wait_people
                wait_people = 0
            temp = num_of_people * boardingCost - c * runningCost
            l.append(temp)
        if max(l) > 0:
            return l.index(max(l)) + 1
        else:
            return -1
