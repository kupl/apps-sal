class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        orig_satisfied_list = [customers[i] * (1-grumpy[i]) for i in range(len(customers))]
        orig_satisfied = sum(orig_satisfied_list)
        grumpy_satisfied_list = [customers[i] - orig_satisfied_list[i] for i in range(len(customers))]
        diff_list = [max(0, grumpy_satisfied_list[i] - orig_satisfied_list[i]) for i in range(len(customers))]
        #print(orig_satisfied_list)
        #print(grumpy_satisfied_list)
        #print(diff_list)
        #print([sum(diff_list[i:i+X]) for i in range(len(customers)-X+1)])
        return orig_satisfied + max([sum(diff_list[i:i+X]) for i in range(len(customers)-X+1)])
