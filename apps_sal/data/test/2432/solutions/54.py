# Python3 code to check if k-th bit 
# of a given number is set or not 

def isKthBitSet(n, k): 
	if n & (1 << (k - 1)): 
		return True
	else: 
		return False

x=int(input())
ans=0
if(isKthBitSet(x,6)):ans+=2**5
if(isKthBitSet(x,5)):ans+=2**0
if(isKthBitSet(x,4)):ans+=2**2
if(isKthBitSet(x,3)):ans+=2**3
if(isKthBitSet(x,2)):ans+=2**1
if(isKthBitSet(x,1)):ans+=2**4
print(ans)
