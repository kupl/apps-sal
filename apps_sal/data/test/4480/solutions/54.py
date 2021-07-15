class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        s1 = 0
        i = 0
        print((s//3))
        while i < len(A):
            s1 += A[i]
            if s1 == s//3:
                break
            i+=1
        s1 = 0
        i+=1
        while i < len(A):
            s1 += A[i]
            print(s1)
            if s1 == s//3:
                if i != len(A)-1:
                    return True
            i+=1
        return False

