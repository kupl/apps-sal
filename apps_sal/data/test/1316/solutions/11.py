import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import defaultdict

n,k = li()
s = ns()

def run_length(s: str):
    ret = []
    buf = ""
    cnt = 0
    for si in s:
        if si != buf:
            if cnt > 0:
                ret.append([buf, cnt])
                
            buf = si
            cnt = 1
        else:
            cnt += 1
            
    ret.append([buf, cnt])
            
    return ret

ret = run_length(s)
        
dic = defaultdict(int)
for char, length in ret:
    dic[char] += length//k
    
ans = 0
for key, value in dic.items():
    ans = max(ans, value)
    
print(ans)
