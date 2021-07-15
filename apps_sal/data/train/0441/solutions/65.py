def sum_up_to(n):
    return n * (n + 1) // 2

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        k = 1
        num_ways = 0
        while k * (k - 1) // 2 < N:
            if  (N - sum_up_to(k - 1)) % k == 0:
                num_ways += 1
            k += 1
        #def compute_floor():
        #    return (N - sum_up_to(k - 1)) // k
        #floor = compute_floor()
        #while floor > 0:
        #    this_sum = sum_up_to(floor + k - 1) - sum_up_to(floor - 1)
        #    if this_sum == N:
        #        num_ways += 1
        #    floor = compute_floor()
        return num_ways

#x + (x+1) + (x+2) + ... + (x+k-1) = N
#k * (k - 1) / 2 = (k**2 - k) / 2 < k**2

