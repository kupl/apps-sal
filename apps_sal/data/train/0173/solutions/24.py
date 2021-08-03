class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for u in arr:
            dic[u % k] += 1
        for i in range(1 + k // 2):
            if i == 0:
                if dic[0] % 2 != 0:
                    return False
            else:
                if dic[i] != dic[k - i]:
                    return False
        return True
