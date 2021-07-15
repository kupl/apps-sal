N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0

for v,c in zip(V,C):
     ans += (v > c)*(v - c)

print(ans)
