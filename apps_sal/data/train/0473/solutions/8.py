class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        scan = [0 for i in arr]
        scan[0] = arr[0]
        for i in range(1, len(arr)):
            scan[i] = scan[i - 1] ^ arr[i]
        res = 0
        for i in range(len(arr)-1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    a = scan[j - 1] ^ scan[i] ^ arr[i]
                    b = scan[k] ^ scan[j - 1]
                    if a == b:
                        res += 1
        return res
            

