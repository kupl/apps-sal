from sys import stdin
import math
N = int(stdin.readline().rstrip())
t,a = [int(x) for x in stdin.readline().rstrip().split()]
 
for _ in range(N-1):
    T,A = [int(x) for x in stdin.readline().rstrip().split()]
    n = max((t + T - 1) // T,(a + A - 1) // A)
    t = n*T
    a = n*A
    
print(t+a)
