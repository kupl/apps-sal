'''
Find an n × n matrix with different numbers from 1 to n^2, 
so the sum in each row, column and both main diagonals are odd.

Input

The only line contains odd integer n (1 ≤ n ≤ 49).

Output

Print n lines with n integers. All the integers should 
be different and from 1 to n2. The sum in each row, 
column and both main diagonals should be odd.
'''

import io
import sys
import time
import random
#~ start = time.clock()
#~ test ='''5
#~ '''

#~ sys.stdin = io.StringIO(test)

n = int(input())
k = n//2
# input is 2k+1

m = [ [1 for j in range(n)] for i in range(n) ]
for i in range(1,k+1):
   for j in range(1,k+2-i):
      m[i-1][j-1] = 0
      m[n-i][j-1] = 0
      m[i-1][n-j] = 0
      m[n-i][n-j] = 0

even_index = 1
odd_index = 1
for i in range(n):
   for j in range(n):
      if m[i][j]==0: # get next even number
         m[i][j] = even_index*2
         even_index += 1
      else:
         m[i][j] = odd_index*2-1
         odd_index += 1
         
for i in range(n):
   for j in range(n):
      print(m[i][j],end=' ')
   print()
         
#~ dur = time.clock()-start
#~ print("Time:",dur)

