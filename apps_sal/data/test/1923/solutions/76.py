n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n):
    ans += l[2*i]
print(ans)
