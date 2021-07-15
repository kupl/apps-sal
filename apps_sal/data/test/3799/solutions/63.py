import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5) 
 
def li(): return list(map(int, stdin.readline().split()))
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return list(map(float, stdin.readline().split()))
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

s = lc()

left = s[0]
right = s[-1]

# aba型のとき
if s[0] == s[-1]:
    if len(s)%2:
        print("Second")
    else:
        print("First")

# ab型のとき    
else:
    if len(s)%2:
        print("First")
    else:
        print("Second")

