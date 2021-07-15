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

students=[]
for i in range(n):
	students.append(lm())

students.sort(key=lambda x: x[1]-x[0])

diss=0

for i in range(n):
	diss+=i*students[i][0]+(n-i-1)*students[i][1]

print(diss)

