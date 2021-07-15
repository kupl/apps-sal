class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        heap = []
        for i in range(lo, hi+1):
            power = self.computer_power(i)
            heapq.heappush(heap, (power, i))
        actual_power = -1
        new_power = -1
        actual_list = []
        result = []
        k_now = 1
        while heap:
            new_power, i = heapq.heappop(heap)
            if k_now == k:
                return i
            k_now += 1
            if new_power != actual_power:
                actual_list.sort()
                result = result + actual_list
                actual_list = [i]
            else:
                actual_list.append(i)
        if actual_list:
            actual_list.sort()
            result = result + actual_list
        return result
    
    def computer_power(self, val):
        if val == 1:
            return 0
        
        if val % 2 == 0:
            return 1 + self.computer_power(val // 2)
        else:
            return 1 + self.computer_power(3*val + 1)
