class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        modulo = [0] * k

        for a in arr:
            modulo[a % k] += 1

        for i in range(1, k):
            if i == k - i and modulo[i] % 2 != 0:
                return False
            elif modulo[i] != modulo[k - i]:
                return False
        return True
