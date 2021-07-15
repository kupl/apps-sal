class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        if len(A) < 2:
            return False
        
        sumA, lenA = sum(A), len(A)
        
        if sumA / lenA in A:
            return True
        
        if len(A) < 3:
            return False
        
        if not any((sumA*size) % lenA == 0 for size in range(1, lenA//2+1)): 
            return False
        
        A = [i * lenA - sumA for i in A]
        A.sort()
        
        a = [i for i in A if i < 0]
        b = [i for i in A if i > 0]
        
        if len(a) > len(b):
            a, b = b, a
        
        d = set()
        def r1(s, arr, n):
            xx = None
            while arr:
                x = arr.pop()
                if xx == x:
                    continue
                
                xx = x
                ss = s + x
                
                d.add(-ss)
                
                if n:
                    r1(ss, list(arr), n-1)

        r1(0, a, len(a) // 2)
        
        def r2(s, arr, n):
            xx = None
            while arr:
                x = arr.pop()
                if xx == x:
                    continue
                
                xx = x
                ss = s + x
                if ss in d:
                    return True
                
                if n and r2(ss, list(arr), n-1):
                    return True
        return r2(0, b, len(b) // 2 - 1)



            

