class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xor = arr.copy()
        for i in range(1,len(xor)):
            xor[i] ^= xor[i-1]
        print([bin(z) for z in arr])
        print([bin(z) for z in xor])
        
        count = 0
        
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                a = xor[j-1] if i == 0 else xor[j-1] ^ xor[i-1]
                for k in range(j,len(arr)):
                    # print(i,j,k)
                    b = xor[k] ^ xor[j-1]
                    # print(a,b)
                    if a == b:
                        # print(\"xxx\")
                        count += 1
        return count
                    
                    

