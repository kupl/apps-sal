class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        happy_owner_cust = 0
        for pos in range(len(customers)):
            if grumpy[pos] == 0:
                happy_owner_cust += customers[pos]
                customers[pos] = 0
        calming_owner_cust = 0
        best_calmed_cust = 0
        for end in range(len(customers)):
            calming_owner_cust += customers[end]
            if end >= X:
                calming_owner_cust -= customers[end - X]
            best_calmed_cust = max(best_calmed_cust, calming_owner_cust)
        return happy_owner_cust + best_calmed_cust


class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        always_happy = 0
        for pos in range(len(customers)):
            if grumpy[pos] == 0:
                always_happy += customers[pos]
                customers[pos] = 0
        happy_use = 0
        cur_happy_customers = 0
        for pos in range(len(customers)):
            cur_happy_customers += customers[pos]
            if pos >= X:
                cur_happy_customers -= customers[pos - X]
            happy_use = max(happy_use, cur_happy_customers)
        return always_happy + happy_use
