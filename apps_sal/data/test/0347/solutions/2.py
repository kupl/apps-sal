M = list(map(int,input().split()))
W = list(map(int,input().split()))
s,e = list(map(int, input().split()))
P = [500,1000,1500,2000,2500]
r = 0
for k in range(5):
    r += max([0.3*P[k],(1-(M[k]/250))*P[k] - 50*W[k]])
print(int(r+100*s-50*e))

