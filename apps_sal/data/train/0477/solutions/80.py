class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        a = [0]
        while k > len(a):
            a.append(1)
            for i in range(len(a) - 2, -1, -1):
                a.append(a[i] ^ 1)
        return str(a[k - 1])
