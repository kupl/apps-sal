n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(len(l)):
    if l[0] < l[i] and l[-1] > l[i]:
        ans += 1
print(ans)
