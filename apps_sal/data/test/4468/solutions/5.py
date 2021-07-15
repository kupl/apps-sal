n,t = map(int,input().split())
T = list(map(int,input().split()))

s = n * t
for i in range(1,n):
    if T[i] - T[i-1] < t:
        s -= (t-(T[i]-T[i-1]))
print(s)
