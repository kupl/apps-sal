n = int(input())
ab = []
cd = []
for i in range(n):
    ab.append(tuple(map(int,input().split())))

for g in range(n):
    cd.append(tuple(map(int,input().split())))

ab.sort(key=lambda x: x[1], reverse = True)
cd.sort()
used = [False]*n

ans = 0
for i in range(n):
    for g in range(n):
        if ab[i][0] < cd[g][0] and ab[i][1] < cd[g][1] and not used[g]:
            used[g] = True
            ans += 1
            break
print(ans)
