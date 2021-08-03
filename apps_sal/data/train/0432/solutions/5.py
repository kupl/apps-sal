class Solution:
  # 456 ms
    def isPossibleDivide(self, nums, k):
        if len(nums) % k:
            return False
        Ct = Counter(nums)
        keys = list(Ct.keys())
        heapify(keys)
        start = heappop(keys)

        while Ct:

            while not Ct[start]:
                start = heappop(keys)
            for i in range(start, start + k):
               # print(num+i)
                if not Ct[i]:
                    return False
                if Ct[i] == 1:
                    del Ct[i]
                else:
                    Ct[i] -= 1

        return True
