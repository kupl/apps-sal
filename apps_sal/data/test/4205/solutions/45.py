N = int(input())
ans = 0
d = [int(s) for s in input().split()]
for i in range(N):
    if d[i] != i + 1:
        ans += 1
if ans >= 3:
    print("NO")
else:
    print("YES")
