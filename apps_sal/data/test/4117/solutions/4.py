n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if l[i] < l[j] < l[k] and l[i] + l[j] > l[k]:
                ans += 1
print(ans)
