class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr) - 1):
            for k in range(len(arr) - 1, i, -1):
                if k == len(arr) - 1:
                    B = arr[k]
                    for z in range(k - 1, i, -1):
                        B ^= arr[z]
                    b = B
                else:
                    B ^= arr[k + 1]
                    b = B
                a = arr[i]
                for j in range(i + 1, k + 1):
                    a ^= arr[j]
                    b ^= arr[j]
                    if a == b:
                        ans += 1
        return ans
