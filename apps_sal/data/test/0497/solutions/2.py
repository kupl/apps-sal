from collections import defaultdict as dd
import math
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))


n=nn()

houses=lm()

start=0

while houses[start]==houses[n-1]:
	start+=1


end=n-1

while houses[end]==houses[0]:
	end-=1


print(max([n-1-start, end]))





