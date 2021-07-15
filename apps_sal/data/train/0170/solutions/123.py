class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        # 1 4 5 2 3 2 1 5 6 7
        # can be removed only in 3 types 
        # last, middle, front
        
        #front - what is the longest sorted array in the suffix
        #last - what is the longest sorted array in the prefix
        #middle - find the prefix and sufix sorting then see if then can be merged else 0
        
        n = len(arr)
        if n==1 or n==0:
            return 0
        front = 0
        a = -1
        b = -1
        last = 0
        middle = 0
        c = 1
        for i in range(1, n):
            if arr[i]>=arr[i-1]:
                c += 1
            else :
                a = i-1
                front = c
                break
        if c == n:
            a = n-1
            front = c
        c = 1
        for i in range(n-1,1,-1):
            if arr[i-1]<=arr[i]:
                c += 1
            else :
                last = c
                b = i
                break
        
        if c == n:
            b = 0
            last = c
        print((front, a, last, b))
        if b !=-1 and a!= -1 :
            for i in range(b,n):
                if arr[a] <= arr[i]:
                    middle = max(middle, front+(n-i))
                print((1,a,i))
            for i in range(0,a+1):
                if arr[i] <= arr[b]:
                    middle = max(middle, last+i+1)
                    print((2,i, b))
                    
                    
        return n-max(last,max(front,middle))

