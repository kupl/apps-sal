import sys,math,collections,itertools
input = sys.stdin.readline

N,A,B,C=list(map(int,input().split()))
l = [ int(input()) for _ in range(N)]

use_list = list(itertools.product(list(range(4)),repeat = N))
point = float('inf')

for i in range(len(use_list)):
    ABC = [0]*3
    count = [0]*3
    if (0 not in use_list[i]) or(1 not in use_list[i]) or (2 not in use_list[i]):
        continue
    for j in range(len(use_list[i])):
        if use_list[i][j] != 3:
            ABC[use_list[i][j]] += l[j]
            count[use_list[i][j]] += 1
    p = (sum(count)-len(count))*10+abs(ABC[0]-A)+abs(ABC[1]-B)+abs(ABC[2]-C)
    point = min(point,p)   
print(point)

