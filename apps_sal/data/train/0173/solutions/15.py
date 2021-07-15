import math

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # count of elements in each class
        moduloclasses = [0] * k
        for n in arr:
            moduloclasses[n % k] += 1
        
        # these two are 2*[n]=0
        # if there's a class in the middle
        # verify that it is even
        if k % 2 == 0 and moduloclasses[k//2] % 2 != 0:
            return False
        # modulo class for 0
        if moduloclasses[0] % 2 !=0:
            return False
        
        for i in range(1, math.ceil(k / 2)):
            # classes and their negatives
            if moduloclasses[i] != moduloclasses[k - i]:
                return False
        
        return True

