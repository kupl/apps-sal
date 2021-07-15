import sys
import math
#from queue import *
#import random
#sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
 
############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input()))
def inara():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(list(map(int,input().split())))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############

s=insr()
ara=["Sunny", "Cloudy", "Rainy", "Sunny", "Cloudy", "Rainy"]

if s[0]=='S':
	print((ara[1]))
elif s[0]=='C':
	print((ara[2]))
else:
	print((ara[0]))

