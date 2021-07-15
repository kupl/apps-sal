N,K = map(int,input().split())
x = list(map(int,input().split()))

ans = []
for i in range(N-K+1):
    if x[i] < 0 and x[i+K-1] > 0:
        ans += abs(x[i]) + abs(x[i+K-1]) + min(abs(x[i]),abs(x[i+K-1])),
    elif x[i] < 0:
        ans += -x[i],
    else:
        ans += x[i+K-1],
print(min(ans))
