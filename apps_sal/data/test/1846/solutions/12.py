# ---------------------------------------------
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
mod = 1000000007
def get_arr(): return list(map(int, input().split()))
def get_int(): return int(input())
def get_ints(): return map(int, input().split())
def get_str(): return input()
def get_strs(): return input().split()
# ---------------------------------------------


n = get_int()
A = get_arr()
pos, neg, ans, temp = 0, 0, sys.maxsize, 0
for i in range(n - 1):
    if A[i] <= 0:
        neg += 1
if(A[-1] <= 0):
    temp += 1

for i in range(n - 1):
    if A[i] <= 0:
        neg -= 1
    if A[i] >= 0:
        pos += 1
    ans = min(ans, pos + neg)
print(ans + temp)
