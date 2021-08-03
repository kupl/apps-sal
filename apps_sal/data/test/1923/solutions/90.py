n = int(input())
n = n * 2
l = list(map(int, input().split()))
l.sort()
l.reverse()
ans = 0
for i in range(len(l)):
    if i % 2 == 1:
        ans += l[i]
print(ans)
