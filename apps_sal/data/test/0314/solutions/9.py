n, m = list(map(int, input().split()))
z = list(map(int, input().split()))
ans = 0
ctr = 0
left = 0
while ctr < m:
    if ans >= n:
        print(-1)
        return
    else:
        z[ans] += left
        ctr += min(8, z[ans])
        left = z[ans] - min(8, z[ans])
    ans += 1
print(ans)

