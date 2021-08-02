N = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for i in range(len(v)):
    if v[i] - c[i] >= 0:
        ans = ans + v[i] - c[i]

print(ans)
