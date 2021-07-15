class Solution:
  # 456 ms
    def isPossibleDivide(self, nums, k):
        if len(nums) % k: return False
        Ct = Counter(nums)
        keys = list(Ct.keys())
        heapify(keys)
        num = heappop(keys)
        
        while Ct:
            while not Ct[num]:
                num = heappop(keys)
            for i in range(k):
               # print(num+i)
                if not Ct[num+i]: return False
                if Ct[num+i] == 1: del Ct[num+i]
                else: Ct[num+i] -= 1
                
        return True
