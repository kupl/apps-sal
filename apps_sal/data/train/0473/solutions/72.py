class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # store=[0]
        # n=len(arr)
        # for i in range(n):
        #     store.append(arr[i]^store[i])
        # ans=0
        # print(store)
        # for i in range(1,n):
        #     for k in range(i+1,n+1):
        #         if store[i-1]==store[k]:
        #             ans+=(k-i)
        # print(7^6)
        # return ans
        n = len(arr)
        c = 0
        for k in range(1,n):
            b=0
            for j in range(k, 0, -1):
                b = b^arr[j]
                a = 0
                for i in range(j-1, -1, -1):
                    a = a^arr[i]
                    #print(i, j, k, \"=>\", a, b)
                    if a==b:
                        c+=1
        return c
