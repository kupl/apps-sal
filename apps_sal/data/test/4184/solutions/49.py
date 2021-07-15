N = int(input())
W = list(map(int, input().split()))

s1 = 0
s2 = 0
s = []
for i in range(N):
    s1 += W[i]
    s2 = sum(W) - s1    
    s.append(abs(s1 - s2))

ans = min(s)
print(ans)
