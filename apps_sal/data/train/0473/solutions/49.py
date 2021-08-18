class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        '''n = len(arr)
        count = 0
        for i in range(n-1):
            for j in range(i+1, n):
                a = arr[i]
                for x in range(i+1, j):
                    a ^= arr[x]
                for k in range(j, n):
                    b = arr[j]
                    for x in range(j+1, k+1):
                        b ^= arr[x]
                    if a == b:
                        count+=1
        return count'''
        n = len(arr)
        c = 0
        for k in range(1, n):
            b = 0
            for j in range(k, 0, -1):
                b = b ^ arr[j]
                a = 0
                for i in range(j - 1, -1, -1):
                    a = a ^ arr[i]
                    if a == b:
                        c += 1
        return c
