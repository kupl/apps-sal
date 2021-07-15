n = list(map(int, list(input())))
k = int(input())

dp0 = [0]*3
dp1 = [[0]*3]*len(n)
dp0[0] = 1
dp1[0][0] = max(0, n[0]-1)
for i in range(1, len(n)):
    dp1[i] = [
        dp1[i-1][0]+dp0[0]*(n[i]!=0)+9,
        dp1[i-1][1]+dp0[1]*(n[i]!=0)+dp0[0]*max(0, n[i]-1)+dp1[i-1][0]*9,
        dp1[i-1][2]+dp0[2]*(n[i]!=0)+dp0[1]*max(0, n[i]-1)+dp1[i-1][1]*9,
    ]
    if n[i] != 0:
        dp0 = [0]+dp0[:2]
print(dp0[k-1]+dp1[-1][k-1])
