class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = arr[i] ^ psum[i]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a = psum[j] ^ psum[i]
                    b = psum[k + 1] ^ psum[j]
                    if a == b:
                        res += 1
        return res
