class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        x= 0
        for i in A:
            x += i
        if x%3 !=0 :
            return False
        x = x/3
        count = 0
        sum1 = 0
        for i in A :
            sum1 += i
            if sum1 == x :
                count += 1
                sum1 = 0
        if count >= 3 :
            return True
        else:
            return False
