N = int(input())
X = list(map(int,input().split()))
T = sum(X) // len(X)
a = 0
b = 0
c = 0
for i in X:
    a += (i - T)**2
    b += (i - T -1)**2
    c += (i - T+1)**2

ans = min(a,b)
print(min(ans,c))
