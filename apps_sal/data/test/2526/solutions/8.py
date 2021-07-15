X,Y,A,B,C = list(map(int,input().split()))
P = sorted(list(map(int,input().split())),reverse=True)[:X]
Q = sorted(list(map(int,input().split())),reverse=True)[:Y]
R = list(map(int,input().split()))

all = P + Q + R

all.sort(reverse=True)

print((sum(all[:X+Y])))

