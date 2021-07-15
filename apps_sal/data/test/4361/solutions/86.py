n,k = list(map(int,input().split()))
h = [int(input()) for _ in range(n)]
h.sort()
d = []
for i in range(n-k+1):
    d.append(abs(h[i] - h[i+k-1]))
print((min(d)))

