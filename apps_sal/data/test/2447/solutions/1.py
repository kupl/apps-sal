import sys, random, math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def main():
    inf = 10 ** 20

    t = int(input())
#    t, a, b = map(int, input().split())
#    t = 1
    
    for _ in range(1, t+1):
    #    print("Case #{}: ".format(_), end = '')
        
        s = input().strip()
        ps0, ps1 = [0], [0]
        for i in range(len(s)):
            if(s[i] == '0'):
                ps0.append(ps0[-1]+1)
                ps1.append(ps1[-1])
            else:
                ps0.append(ps0[-1])
                ps1.append(ps1[-1]+1)
        ans = inf
        for i in range(len(s)):
            ans = min(ans, (ps0[i] - ps0[0]) + (ps1[len(s)] - ps1[i]))
            ans = min(ans, (ps1[i] - ps1[0]) + (ps0[len(s)] - ps0[i]))
        
        print(ans)
        
main()
