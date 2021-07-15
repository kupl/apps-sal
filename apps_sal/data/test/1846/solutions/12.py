#---------------------------------------------
import sys 
sys.stdin = open('input.txt', 'r'); sys.stdout = open('output.txt', 'w')
mod = 1000000007
get_arr = lambda: list(map(int, input().split()))
get_int = lambda: int(input())
get_ints = lambda: map(int, input().split())
get_str = lambda: input()
get_strs = lambda: input().split()
#---------------------------------------------

n = get_int()
A = get_arr()
pos, neg, ans, temp = 0, 0, sys.maxsize, 0
for i in range(n-1):
    if A[i]<=0: neg += 1
if(A[-1]<=0): temp += 1

for i in range(n-1):
    if A[i] <=0: neg -= 1
    if A[i] >=0: pos += 1
    ans = min(ans, pos+neg)
print(ans+temp)
