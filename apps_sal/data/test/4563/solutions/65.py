from sys import stdin
import math
N = int(stdin.readline().rstrip())
t,a = 1,1
 
for _ in range(N):
    T,A = [int(x) for x in stdin.readline().rstrip().split()]
    n = max((t + T - 1) // T,(a + A - 1) // A)
    t = n*T
    a = n*A
    
print(t+a)
