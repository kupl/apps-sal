class Solution:
    def minOperationsMaxProfit(self, customers: List[int], bc: int, rc: int) -> int:
        li = [0, ]
        wait = 0
        for i in customers:
            i += wait
            wait = 0
            if i > 4:
                wait = i - 4
            li.append(li[-1] + min(4, i) * bc - rc)
        while wait > 0:
            if wait > 4:
                li.append(li[-1] + 4 * bc - rc)
                wait -= 4
            else:
                li.append(li[-1] + wait * bc - rc)
                wait = 0
        temp = li.index(max(li))
        if temp == 0:
            return -1
        else:
            return temp
