class Solution:

    def canArrange(self, A: List[int], k: int) -> bool:
        counter = Counter()
        for a in A:
            counter[a % k] += 1
        if counter[0] & 1 != 0:
            return False
        for i in range(1, k // 2 + 1):
            if counter[i] != counter[k - i]:
                return False
        return True
