class Solution:
  # 476 ms
    def isPossibleDivide(self, nums, k):
        if len(nums) % k: return False
        c = Counter(nums)
        heapify(nums)

        for _ in range(len(nums) // k):
            num = heappop(nums)
            while not c[num]:
                num = heappop(nums)
            for i in range(k):
               # print(num+i)
                if not c[num+i]: return False
                c[num+i] -= 1

        return True
