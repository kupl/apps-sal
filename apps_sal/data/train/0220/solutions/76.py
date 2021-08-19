class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        L = len(grumpy)
        if L == X:
            return sum(customers)
        tempCustomers = customers.copy()
        grummpyCustomer = [0 if grumpy[i] == 1 else customers[i] for i in range(L)]
        for i in range(1, L):
            tempCustomers[i] += tempCustomers[i - 1]
        for i in range(1, L):
            grummpyCustomer[i] += grummpyCustomer[i - 1]
        result = 0
        maxSum = grummpyCustomer[-1]
        for i in range(X, L):
            result = max(result, tempCustomers[i] - tempCustomers[i - X] + maxSum - grummpyCustomer[i] + grummpyCustomer[i - X])
        grummpyCustomer = [0 if grumpy[i] == 1 else customers[i] for i in range(L)]
        tempCustomers = customers.copy()
        for i in reversed(list(range(L - 1))):
            tempCustomers[i] += tempCustomers[i + 1]
        for i in reversed(list(range(L - 1))):
            grummpyCustomer[i] += grummpyCustomer[i + 1]
        maxSum = grummpyCustomer[0]
        for i in reversed(list(range(L - X))):
            result = max(result, tempCustomers[i] - tempCustomers[i + X] + maxSum - grummpyCustomer[i] + grummpyCustomer[i + X])
        return result
