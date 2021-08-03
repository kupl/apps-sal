class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        b = k // 26
        budget = {i: b + (i <= (k % 26)) for i in range(1, 26)}

        for i, j in zip(s, t):
            shift = (ord(j) - ord(i)) % 26
            if i != j:
                if shift > k:
                    return False
                if budget[shift] == 0:
                    return False
                else:
                    budget[shift] -= 1

        return True
