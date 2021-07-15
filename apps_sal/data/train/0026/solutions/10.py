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
	n,m=lint()
	if n==1 or m==1:
		print("YES")
	elif n==2 and m==2:
		print("YES")
	else:
		print("NO")
	#solve

t=int(input())

########################################################
for i in range(t):                                     #
	#print("Case #"+str(i+1)+":",end=" ")		       #
	main()                                             #
