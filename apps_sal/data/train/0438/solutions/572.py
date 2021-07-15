class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        slots = [0 for _ in arr]
        num_m = 0
        last_m = -1 
        if len(arr) == 1:
            if m == 1:
                return 1
            else:
                return -1 
        for n in range(len(arr)):
            i = arr[n]
            idx = i -1 
            if idx == len(arr) - 1:
                slots[idx] = slots[idx - 1] + 1
                if slots[idx] == m:
                    num_m += 1
                if slots[idx - 1] == m:
                    num_m -= 1                    
                if slots[idx - 1] > 0:
                    slots[idx - slots[idx - 1]] = slots[idx]
                
            elif idx == 0:
                slots[idx] = slots[idx + 1] + 1
                if slots[idx] == m:
                    num_m += 1
                if slots[idx + 1] == m:
                    num_m -= 1  
                if slots[idx + 1] > 0:
                    slots[idx + slots[idx + 1]] = slots[idx]
            else:
                slots[idx] = slots[idx- 1] + slots[idx + 1]+ 1
                if slots[idx] == m:
                    num_m += 1
                if slots[idx + 1] == m:
                    num_m -= 1
                if slots[idx - 1] == m:
                    num_m -= 1    
                slots[idx - slots[idx - 1]] = slots[idx]
                slots[idx + slots[idx + 1]] = slots[idx]
            if num_m > 0:
                last_m = n + 1

        return last_m
                

