import numpy as np


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        customers = np.array(customers)
        grumpy = np.array(grumpy)
        total_customers = np.sum(customers)
        grumpy_array = customers * grumpy
        secret_array = np.convolve(grumpy_array, np.ones(X, dtype=int), 'valid')
        index = np.where(secret_array == secret_array.max())[0][0]
        grumpy_array[index:index + X] = 0
        satisfied_customers = total_customers - grumpy_array.sum()
        return satisfied_customers
