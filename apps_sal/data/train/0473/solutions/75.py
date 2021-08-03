class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        c = 0
        for k in range(1, n):
            b = 0
            for j in range(k, 0, -1):
                b = b ^ arr[j]
                a = 0
                for i in range(j - 1, -1, -1):
                    a = a ^ arr[i]
                    # print(i, j, k, \"=>\", a, b)
                    if a == b:
                        c += 1
        return c
