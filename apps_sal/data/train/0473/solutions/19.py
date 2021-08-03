class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preXor = [0] * (len(arr) + 1)
        preXor[0] = arr[0]
        for i in range(1, len(arr)):
            preXor[i] = preXor[i - 1] ^ arr[i]
        ret = 0
        for i in range(len(arr) - 1):
            l = preXor[i - 1]
            for k in range(i + 1, len(arr)):
                if l == preXor[k]:
                    ret += k - i
        return ret
