N = int(input())
h = list(map(int,input().split()))
ans = h[0]
bottom = 0
for i in range(0,len(h)-1):
    if h[i] <= h[i+1]:
        ans += h[i+1] - h[i]
    else:
        continue

print(ans)
