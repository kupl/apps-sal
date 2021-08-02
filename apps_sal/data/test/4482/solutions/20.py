n = int(input())
a = [int(x) for x in input().split()]
a.sort()
ans = []
for i in range(a[0], a[-1] + 1):
    cnt = 0
    for j in range(n):
        cnt += (a[j] - i)**2
    ans.append(cnt)

print(min(ans))
