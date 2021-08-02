
f = [0] * 7
f[1], f[2] = [int(x) for x in input().split()]
f[3] = f[2] - f[1]
f[4] = -f[1]
f[5] = -f[2]
f[6] = -f[3]
n = int(input())
t = n % 6
if(t == 0):
    t = 6
print((f[t]) % 1000000007)
