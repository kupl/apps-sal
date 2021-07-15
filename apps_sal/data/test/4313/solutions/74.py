n = int(input())
v = [int(s) for s in input().split()]
c = [int(s) for s in input().split()]

ans = 0
for i in range(n):
    if v[i] - c[i] > 0:
        ans += v[i] - c[i]
print(ans) 
