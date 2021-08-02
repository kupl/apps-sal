n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    k = i
    for j in range(i + 1, n):
        while k < n and l[k] < l[i] + l[j]:
            k += 1
        ans += k - (j + 1)
print(ans)
