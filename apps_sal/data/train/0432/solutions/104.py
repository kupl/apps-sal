class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for j in d:
            while d[j] > 0:
                for x in range(j, j + k):
                    if d.get(x, 0) > 0:
                        d[x] -= 1
                    else:
                        return False
        return True
        '\n        i=0\n        while k<=len(nums):\n            a=nums[0]\n            for j in range(k):\n                if a+j not in nums or len(nums)==0:\n                    return False\n                nums.remove(a+j)\n            if len(nums)%k!=0:\n                return False\n            if len(nums)==0:\n                return True\n        return True\n        \n        while True :\n            a=nums[0]\n            for i in range(k):\n                if a+i not in nums or len(nums)==0:\n                    return False\n                nums.remove(a+i)\n            if len(nums)%k!=0:\n                return False\n            if len(nums)==0:\n                return True\n        '
