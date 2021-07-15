import sys
import math

def input():
    return sys.stdin.readline().strip()
def iinput():
    return int(input())
def tinput():
    return input().split()
def rinput():
    return list(map(int, tinput()))
def rlinput():
    return list(rinput())

def main():
    res1, res2, res12, o, res = 0, 0, 0, 0, []
    s = list(input())
    n = len(s) - 2
    
    
    
    
    while o < n - 2:
        if s[o] == 't' and s[o + 1] == 'w' and s[o + 2] == 'o' and s[o + 3] == 'n' and s[o + 4] == 'e':
            res12 += 1
            res.append(o + 3)
            o += 5
 
        elif s[o] == 'o' and s[o + 1] == 'n' and s[o + 2] == 'e':
            res1 += 1
            res.append(o + 2)
            o += 3
        elif s[o] == 't' and s[o + 1] == 'w' and s[o + 2] == 'o':
            res2 += 1
            res.append(o  +2)
            o += 3
        else:
            o += 1
            
            
            
            
            
    while o < n:
        if s[o] == 'o' and s[o + 1] == 'n' and s[o + 2] == 'e':
            res1 += 1
            res.append(o + 2)
            o += 3
        elif s[o] == 't' and s[o + 1] == 'w' and s[o + 2] == 'o':
            res2 += 1
            res.append(o + 2)
            o += 3
        else:
            o += 1
    print(res1 + res2 + res12)
    print(*res)
    
for i in range(iinput()):
    main()

