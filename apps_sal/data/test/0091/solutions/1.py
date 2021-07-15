from sys import stdin,stdout                           #
import math                                            #
import heapq                                           #
                                                       #
t = 1                                                  #
def aint():                                            #
	return int(input().strip())                        #
def lint():                                            #
	return list(map(int,input().split()))              #
def fint():                                            #
	return list(map(int,stdin.readline().split()))     #
                                                       #	
########################################################

def main():
	n,k=map(int,input().split())
	cnt=[0]*100
	for i in lint():
		for j in range(60):
			cnt[j]+=i%k
			i//=k
	for i in cnt:
		if i>1:
			print("NO")
			break
	else:
		print("YES")

t=int(input())

########################################################
for i in range(t):                                     #
	main()                                             #
