class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = collections.defaultdict(int)
        for i in range(len(arr)):
            if arr[i] % k != 0:
                dic[arr[i] % k] += 1
        for ki in list(dic.keys()):
            if ki != 0:
                if dic[ki] != dic[k - ki] or (2 * ki == k and dic[ki] % 2 == 1):
                    return False
        return True
