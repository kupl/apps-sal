class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0]*(len(arr)+1)
        prefix[1] = arr[0]
        res = 0
        for i in range(1, len(arr)):
            prefix[i+1] = prefix[i]^arr[i]
        print(prefix)
        for i in range(len(arr)-1):
            for j in range(i, len(arr)):
                if prefix[j+1]^prefix[i] == 0:
                    res+=(j-i)

        return res
