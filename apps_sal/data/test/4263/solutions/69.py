import sys
input = sys.stdin.readline

def slove():
    S = input()
    n = len(S)
    l = 0
    ans = 0
    for i in range(n):
        if S[i]=="A" or S[i]=="C" or S[i]=="G" or S[i]=="T":
            l += 1
        else:
            ans = max(ans,l)
            l = 0
    ans = max(ans,l)
    print(ans)

def __starting_point():
    slove()
__starting_point()
