n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = 0

for i in range(n):
    temp = v[i] - c[i]
    if temp > 0:
        ans += temp
print(ans)
