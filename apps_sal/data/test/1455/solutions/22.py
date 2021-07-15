from collections import defaultdict as dd
import math
import sys
input=sys.stdin.readline
def nn():
	return int(input())

def li():
	return list(input())

def mi():
	return list(map(int, input().split()))

def lm():
	return list(map(int, input().split()))

n=nn()

size=(n+2)//2

print(size)


for i in range(size):
	print(1, i+1)

for j in range(n-size):
	print(j+2,size)







