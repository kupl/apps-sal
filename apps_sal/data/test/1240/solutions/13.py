n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    l[i] = l[i][0] - l[i][1]
ans = 0
su = sum(l)
ma = abs(su)
for i in range(n):
    if abs(su - l[i] - l[i]) > ma: ma = abs(su - l[i] - l[i]); ans = i + 1
print(ans)
