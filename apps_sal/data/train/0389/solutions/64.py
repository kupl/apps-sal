class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        # A = [53,6,3,34,91,82,47,9,70,1]
        if len(A) < 3:
            return False
        
        sumA, lenA = sum(A), len(A)
        
        if sumA / lenA in A:
            return True
        
        A = [i * lenA - sumA for i in A]
        A.sort()
        
        a = [i for i in A if i < 0]
        b = [i for i in A if i > 0]
        
        if len(a) > len(b):
            a, b = b, a
        
        d = {-i for i in A}
        def r(s, arr, n):
            xx = None
            while arr:
                x = arr.pop()
                if xx == x:
                    continue
                
                xx = x
                ss = s + x
                if ss in d:
                    return True
                
                d.add(-ss)
                
                if n and r(ss, list(arr), n-1):
                    return True

        # print(a)
        if r(0, a, len(a) - 1):
            return True
        # print(d)
        # print(b)
        if r(0, b, len(b) // 2 - 1):
            return True
        # print(d)
        return False


            

