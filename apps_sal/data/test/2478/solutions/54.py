def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()
    N = int(input())
    S = input()
    
    #solve
    right=0
    left=0

    for i in range(N):
        if S[i]=='(':
            right+=1
        else:
            if right:
                right-=1
            else:
                left+=1
    print(left*'('+S+right*')')

def __starting_point():
    main()
__starting_point()
