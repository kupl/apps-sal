class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        (arr, ans, curr) = ([1] + [0] * K, 0, 0)
        for i in A:
            curr = (curr + i) % K
            ans += arr[curr]
            arr[curr] += 1
        return ans
