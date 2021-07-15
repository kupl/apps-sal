import sys
def main():
    input = sys.stdin.readline
    K=int(input())
    N=50
    ans=[]
    m=K%N
    for i in range(N):
        t = N-1 + K//N
        ans.append(t)
    for i in range(m):
        for j in range(N):
            if i==j: ans[j]+=N
            else: ans[j]-=1
    print(N)
    print(*ans)

def __starting_point():
    main()
__starting_point()
