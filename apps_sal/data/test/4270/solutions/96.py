N = int(input())
v = list(map(int, input().split()))
v.sort()
ans = v[0]

for i in range(N-1):
    ans = (ans+v[i+1]) / 2

print(ans)
