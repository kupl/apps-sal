n = int(input())
h = [int(i) for i in input().split()]
ans = h[0]
for i in range(1,n):
    if h[i] > h[i-1]:
        ans += h[i] - h[i-1]
print(ans)
