import sys


def main():
    
    n = int(sys.stdin.readline())
    s = list(map(int, sys.stdin.readline().split()))
    ans=1
    cur = 1
    for i in range(1,n):
        if s[i]>s[i-1]:
            cur+=1
        else:
            if cur>ans:
                ans=cur
            cur=1
    if cur>ans:
        ans=cur
            
    print(ans)
    

main()
