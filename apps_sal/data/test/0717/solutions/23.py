import math

n = int(input())
sd = [tuple(map(int,input().split())) for _ in range(n)]
cd = 1

for i in range(n):
    s = sd[i][0]
    d = sd[i][1]
    if s>=cd:
        cd = s
    else:
        cd=s+math.ceil((cd-s)/d)*d
    cd+=1

cd-=1
print(cd)
