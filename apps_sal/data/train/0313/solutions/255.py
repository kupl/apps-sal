class Solution:
    def is_good(self, day):
        bouqet_count = 0
        cont_count = 0
        for d in self.bloomDay:
            if d <= day:
                cont_count += 1
            else:
                bouqet_count += cont_count // self.k
                cont_count = 0
        bouqet_count += cont_count // self.k
        return bouqet_count >= self.m
        
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        self.bloomDay = bloomDay
        self.m = m
        self.k = k
        
        if m * k > len(bloomDay):
            return -1
        start = 1
        end = 10**9
        
        
        while start != end:
            middle = (start + end) // 2
            if self.is_good(middle):
                end = middle
            else:
                start = middle + 1
        
        return start
