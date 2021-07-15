n = int(input())
a = list(map(int, input().split()))
ans, s = 0, a.count(1)
for i in range (n):
    for j in range (i + 1, n + 1):
        tmp = a[i:j].count(0) - a[i:j].count(1)
        if s + tmp > ans: ans = s + tmp
print(ans)
