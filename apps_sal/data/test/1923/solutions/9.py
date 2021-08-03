n = int(input())
l = [int(i) for i in input().split()]
l.sort()
ans = 0
for i in range(0, 2 * n, 2):
    ans += l[i]
print(ans)
