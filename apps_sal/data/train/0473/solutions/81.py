class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        s = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            s[i] = s[i - 1] ^ arr[i - 1]
        ans = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if s[k + 1] ^ s[j] == s[j] ^ s[i]:
                        ans += 1
        return ans
