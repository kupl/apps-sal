n,k = map(int,input().split())
S = list(map(int,input().split()))

t = n - k
m = 0
for i in range(n):
    if i < t:
        s = S[i] + S[2*t - 1 - i]
    elif i < 2*t:
        continue
    else:
        s = S[i]
    if s > m:
        m = s
print(m)
