import sys
import numpy as np
input = sys.stdin.readline

def slove():
    N = int(input())
    town_position = np.array([list(map(float,input().split())) for i in range(N)])
    distance = 0
    for i in range(N-1):
        x1, y1 = town_position[i]
        for j in range(i+1,N):
            x2, y2 = town_position[j] 
            distance += np.sqrt((x2-x1)**2 + (y2-y1)**2)
            
    ans = distance * 2 / N
    print(ans)

def __starting_point():
    slove()
__starting_point()
