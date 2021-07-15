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

total=0

for i in range(n-2):
	total=total+1*(i+2)*(i+3)

print(total) 

