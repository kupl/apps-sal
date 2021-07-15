import sys
def main():
    input = sys.stdin.readline
    K=int(input())
    N=50
    ans=[]
    m=K%N
    for i in range(N):
        t = K//N + (1 if i<m else 0)
        ans.append(N*(t+1) - (K-t) - 1)
    print(N)
    print(*ans)

def __starting_point():
    main()
__starting_point()
