def R(): return list(map(int, input().split()))


n = int(input())
a = []
for _ in range(n):
    a.append(R())
a.sort(key=lambda x: (x[0] + x[1]))
j = 0
ans = 1
for i in range(1, n):
    if a[j][0] + a[j][1] <= a[i][0] - a[i][1]:
        ans += 1
        j = i
print(ans)
