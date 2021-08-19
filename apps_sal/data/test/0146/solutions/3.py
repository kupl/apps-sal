# = list(map(int, input().split()))
# = map(int, input().split())
n, k = list(map(int, input().split()))
z = list(map(int, input().split()))
ans = -1
for b in range(n):
    tans = 0
    for s in range(n):
        if (s - b) % k != 0:
            tans += z[s]
    if abs(tans) > ans:
        ans = abs(tans)
print(ans)
