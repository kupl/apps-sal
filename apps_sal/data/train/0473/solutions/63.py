class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        xors = [0] * (n + 1)
        for z in range(n):
            xors[z] = xors[z-1] ^ arr[z] 
    
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if xors[i - 1] ^ xors[k] == 0:
                        res += 1
                
        return res
                

