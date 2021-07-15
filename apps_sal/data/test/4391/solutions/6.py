n, k = map(int,input().split())
s = [int(i) for i in input().split()]
p  = [0] * (n+1)
for i in range(1, n+1):
    p[i] = p[i-1] + s[i-1]
ma = -5000
for i in range(k, n+1):
    for j in range(k, n+1):
        sred = (p[j] - p[j-i])/i
        if sred > ma:
            ma = sred
print(ma)
