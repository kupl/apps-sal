n,k = map(int, input().split())
h = sorted(list(int(input()) for _ in range(n)))
ans = []
for i in range(n-k+1):
    ans.append(h[i+k-1]-h[i])
print(min(ans))
