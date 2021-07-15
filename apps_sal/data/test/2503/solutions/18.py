import sys
import numpy as np
def main():
    input = sys.stdin.readline
    def gen_pattern(x):
        if x < K-1:
            return [[0, x+1], [x+K+1, 2*K]]
        else:
            return [[x-K+1, x+1]]
    def inputs():
        return [int(x) for x in input().split()]
    def inputstr():
        return list(input().split())
    N,K = inputs()
    BB = [[0]*(2*K+1) for _ in range(2*K+1)]
    for i in range(N):
        x,y,c = inputstr()
        if c=="W":
            y = int(y)+K
        x = int(x)%(2*K)
        y = int(y)%(2*K)
        #BB[x,y] += 1
        for shift in [0,K]:
            for b,t in gen_pattern((y+shift)%(2*K)):
                for l,r in gen_pattern((x+shift)%(2*K)):
                    BB[b][l] +=1
                    BB[b][r] -=1
                    BB[t][l] -=1
                    BB[t][r] +=1
    ans = (np.max(np.cumsum(np.cumsum(BB, axis=1), axis=0)))
    #print(BB)
    print((int(ans)))
main()

