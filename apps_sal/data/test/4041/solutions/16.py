# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import math
from math import gcd,sqrt

def isSubSequence(str1,str2,m,n): 
      
    j = 0    # Index of str1 
    i = 0    # Index of str2 
      
    # Traverse both str1 and str2 
    # Compare current character of str2 with  
    # first unmatched character of str1 
    # If matched, then move ahead in str1 
      
    while j<m and i<n: 
        if str1[j] == str2[i]:     
            j = j+1    
        i = i + 1
          
    # If all characters of str1 matched, then j is equal to m 
    return j==m

#T = int(input())
#N = int(input())
s1 = input()
N = len(s1)
s2 = input()
#N,M,Q = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

res = 0
for i in range(N):
    for j in range(i,N):
        s = s1[:i] + s1[(j+1):]
        # check subsequence
        #print(s)
        if isSubSequence(s2,s,len(s2),len(s)):
            res = max(res,j-i+1)
            
print(res)

