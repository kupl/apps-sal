class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0 for _ in range(len(arr))]
        prefix[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = arr[i] ^ prefix[i-1]
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j, len(arr)):
                    a = prefix[j-1] ^ prefix[i-1] if i >= 1 else prefix[j-1]
                    b = prefix[k] ^ prefix[j-1]
                    res += (a == b)
        return res
