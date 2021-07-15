import math  
def findNumberOfDigits(n, b): 
    dig = (math.floor(math.log(n) /math.log(b)) + 1) 
    return dig
n, k = map(int, input().strip().split())
print(findNumberOfDigits(n, k))
