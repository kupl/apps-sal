class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        preXor = [0] * (len(arr) + 1)
        preXor[0] = arr[0]
        for i in range(1, len(arr)):
            preXor[i] = preXor[i - 1] ^ arr[i]
        ret = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                l = preXor[i - 1]
                for k in range(j, len(arr)):
                    #print(i, j, k)
                    if l == preXor[k]:
                        # print(\"match:\", i, j, k)
                        ret += 1
        return ret
