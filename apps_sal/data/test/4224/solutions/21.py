n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    while l[i] % 2 == 0:
        ans += 1
        l[i] /= 2
print(ans)
