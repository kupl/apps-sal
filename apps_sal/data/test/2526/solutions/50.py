X,Y,A,B,C =map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
R = list(map(int,input().split()))

P.sort()
Q.sort()
R.sort()

P_new = P[-X::]
Q_new = Q[-Y::]


agg = P_new + Q_new +R
agg.sort()
print(sum(agg[-X-Y::]))
