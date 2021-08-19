class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        print(len(arr[:-1]))
        for key1 in range(len(arr[:-1])):
            a = 0
            for (key2, j) in enumerate(arr[key1:]):
                a ^= j
                b = 0
                for k in arr[key2 + key1 + 1:]:
                    b ^= k
                    if b == a:
                        ans += 1
        return ans
