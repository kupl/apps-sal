from collections import defaultdict
H,W,N = map(int,input().split())
d = defaultdict(int)
def process(y,x):
    nonlocal d
    for nowy in range(y-1,y+2):
        for nowx in range(x-1,x+2):
            if 1<=nowy<H-1 and 1<=nowx<W-1:
                d[(nowy,nowx)] += 1


for i in range(N):
    a,b = map(int,input().split())
    process(a-1,b-1)

num_black = [0] * 10
for value in d.values():
    num_black[value] += 1
num_black[0] = max(0,(H-2)*(W-2)-sum(num_black))
for i,a in enumerate(num_black):
    print(a)
