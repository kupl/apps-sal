class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prexor = [0]
        for num in arr:
            prexor.append(prexor[-1] ^ num)

        # print(prexor)
        cnt = 0
        # result = []
        for i in range(1, len(arr) + 1):
            for j in range(i + 1, len(arr) + 1):
                for k in range(i + 1, j + 1):
                    if prexor[k - 1] ^ prexor[i - 1] == prexor[j] ^ prexor[k - 1]:
                        # result.append([i-1, k-1, j-1])
                        cnt += 1
        # print(result)
        return cnt
