class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        dic = Counter(nums)
        key = list(sorted(dic.keys()))
        while key:
            last = -1
            remove = []
            if len(key) < k:
                return False
            for (i, num) in enumerate(key):
                if i == k:
                    break
                if last == -1:
                    last = num
                    dic[num] -= 1
                elif num - last == 1 and i < k:
                    last = num
                    dic[num] -= 1
                elif num - last != 1:
                    return False
                if dic[num] == 0:
                    remove.append(i)
            remove.sort(reverse=True)
            for ind in remove:
                key.pop(ind)
        return True
